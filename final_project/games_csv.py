import csv
import glob
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class Game:
    id: UUID
    title: str
    publisher: str
    parental_guidance: str
    release_date: str
    updated_at: datetime
    price: int
    genre: str
    system: str
    discount: int


csv_files = glob.glob("*.csv")
games: dict[str, Game] = {}
for csv_file in csv_files:
    with open(csv_file, "r") as file, open(
        "games_consolidation.csv", "a"
    ) as csv_consolidation_file:
        reader = csv.reader(file)
        writer = csv.writer(csv_consolidation_file)
        for i, line in enumerate(reader):
            if line[6] == "release date":
                continue

            if line[0] in games:
                continue

            release_date = "2024-09-18"
            try:
                print(line[6])
                release_date = datetime.strptime(line[6], "%d %b, %Y").strftime(
                    "%Y-%m-%d"
                )
            except ValueError:
                print(line[6])
                release_date = datetime.strptime(line[6], "%b %d, %Y").strftime(
                    "%Y-%m-%d"
                )

            game = Game(
                id=uuid4(),
                title=line[1],
                parental_guidance=line[2],
                publisher=line[3],
                genre=line[4],
                price=line[5],
                release_date=release_date,
                system=line[7],
                discount=5,
                updated_at=datetime.now(),
            )
            writer.writerow(
                [
                    game.id,
                    game.title,
                    game.parental_guidance,
                    game.publisher,
                    game.genre,
                    game.price,
                    game.release_date,
                    game.updated_at.isoformat(),
                    game.system,
                    game.discount,
                ]
            )
            games[line[0]] = game

        print(games.keys())
