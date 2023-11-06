import psycopg2

con = psycopg2.connect(database='bank', user='root', password='12345678')

with con:
    cur = con.cursor()
    cur.execute("select * from bank.bank")

    rows = cur.fetchall()

    for row in rows:
        print(f"{row[0]} {row[1]} {row[2]}")