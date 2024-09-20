import csv

with open("games_consolidation.csv", "r") as csv_file, open(
    "products_insert.sql", "w"
) as sql_file, open("prod_price", "w") as prod_file:
    reader = csv.reader(csv_file)
    sql_file.write(
        "INSERT INTO products (id, title, publisher, parental_guidance, release_date, updated_at, price, genre, system, discount) VALUES "
    )
    prod_file.write("[\n")
    for game in reader:
        title = game[1].replace("'", "''")
        publisher = game[3].replace("'", "''")
        sql_file.write(
            f"('{game[0]}', '{title}', '{publisher}', '{game[2]}', '{game[6]}', '{game[7]}', {game[5]}, '{game[4]}', '{game[8]}', {game[9]}),\n"
        )
        prod_file.write(f'\t("{game[0]}", {game[5]}),\n')
    prod_file.write("]\n")
