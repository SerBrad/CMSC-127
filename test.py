import mysql.connector
from decimal import Decimal

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
    for row in mycursor:
        formatted_row = [str(item) if isinstance(item, Decimal) else item for item in row]
        print(formatted_row)
else:
    print("Not")
