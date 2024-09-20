from uuid import uuid4

from faker import Faker

fake = Faker("pt_BR")


with open("users_insert.sql", "w") as sql_file:
    sql_file.write(
        "INSERT INTO users (id, first_name, last_name, username, gender, cpf, birth_date) VALUES\n"
    )
    for _ in range(100):
        sql_file.write(
            f"('{uuid4()}', '{fake.first_name()}', '{fake.last_name()}', '{fake.user_name()}', '{fake.passport_gender()}', '{fake.cpf()}', '{fake.date_of_birth().strftime('%Y-%m-%d')}'),\n"
        )
