import mysql.connector
from decimal import Decimal
from datetime import datetime, date
from tabulate import tabulate

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3307,
    password="brad",
    database="transactions"  # Replace with the actual database name
)

if mydb:
    print("Connection Successful")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM transaction;")
    rows = mycursor.fetchall()
    headers = [desc[0] for desc in mycursor.description]

    formatted_rows = []
    for row in rows:
        formatted_row = []
        for item in row:
            if isinstance(item, Decimal):
                formatted_row.append(float(item))
            elif isinstance(item, datetime):
                formatted_row.append(item.date())
            else:
                formatted_row.append(item)
        formatted_rows.append(formatted_row)

    print(tabulate(formatted_rows, headers, tablefmt="grid"))
else:
    print("Not")
