import concurrent
import concurrent.futures
import csv
from dataclasses import dataclass
from enum import Enum
from random import choices
from time import sleep
from typing import Optional
from urllib.parse import urljoin

import requests

STEAM_API_BASE_URL = "https://api.steampowered.com"
STEAM_STORE_API_BASE_URL = "https://store.steampowered.com/"


class System(Enum):
    Playstation = "playstation"
    Nintendo = "nintendo"
    PC = "pc"


@dataclass
class AppDetails:
    required_age: int
    publisher: str
    price: int
    genre: str
    release_date: str
    system: System


@dataclass
class App:
    id: int
    name: str
    details: Optional[AppDetails]


def get_app_list() -> list[App]:
    resp = requests.get(
        urljoin(STEAM_API_BASE_URL, "/ISteamApps/GetAppList/v2/?format=json")
    )
    resp.raise_for_status()
    resp_body: dict = resp.json()
    app_list: dict = resp_body["applist"]
    apps: list[App] = []
    for app in app_list["apps"]:
        if app.get("name"):
            apps.append(App(id=app.get("appid"), name=app.get("name"), details=None))
    return apps


def get_app_details(app: App) -> Optional[App]:
    print(f"Getting details for app {app.id} - {app.name}")
    resp = requests.get(
        urljoin(STEAM_STORE_API_BASE_URL, f"/api/appdetails?appids={app.id}")
    )

    if not resp.ok:
        print(resp.headers)
        print(f"Got status: {resp.status_code}")
        return None

    resp_body: dict = resp.json()
    details = resp_body[str(app.id)]
    if not details["success"]:
        return None

    data = details["data"]

    price = data.get("price_overview", {}).get("final")
    if not price:
        return None

    if not data.get("publishers"):
        return None

    if not data.get("genres"):
        return None

    ratings: dict = data.get("ratings", {})
    if not ratings:
        return None

    age = 0
    if ratings.get("dejus"):
        age = ratings.get("dejus").get("rating")
    elif ratings.get("usk"):
        age = ratings.get("usk").get("rating")

    system = choices([s for s in System])[-1]

    app.details = AppDetails(
        age,
        data["publishers"][0],
        price,
        data["genres"][0]["description"],
        data["release_date"]["date"],
        system=system,
    )

    print(f"Finished getting details for app {app.id} - {app.name}")

    return app


def create_game_csv():
    app_list = get_app_list()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor, open(
        "games.csv", "a"
    ) as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            [
                "appid",
                "name",
                "required age",
                "publisher",
                "genre",
                "price",
                "release date",
                "system",
            ]
        )
        futures = [executor.submit(get_app_details, a) for a in app_list[:2000]]
        for future in concurrent.futures.as_completed(futures):
            app = future.result()
            if app:
                writer.writerow(
                    [
                        app.id,
                        app.name,
                        app.details.required_age,
                        app.details.publisher,
                        app.details.genre,
                        app.details.price,
                        app.details.release_date,
                        app.details.system.value,
                    ]
                )


if __name__ == "__main__":
    create_game_csv()
