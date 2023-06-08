import mysql.connector
from decimal import Decimal
from datetime import datetime, date
from tabulate import tabulate

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3307, # Replace with the correct port number for your setup
    password="brad",
    database="transactions"  # Replace with the actual database name
)

def searchFriend():
    friendID = input("Please enter a friendID: ")
    print("Connection Successful")
    mycursor = mydb.cursor()

    sqlQuery =  "SELECT username FROM user JOIN befriends ON (user.userid = befriends.user1id OR user.userid = befriends.user2id) AND user.userid != 1 AND user.username = 'James'"
    mycursor.execute(sqlQuery)
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

def print_menu():
    print("-------------------------------")
    print("        CMSC 127 PROJECT")
    print(" 1-Add, delete, search, and update an expense ")
    print(" 2-Add, delete, search, and update a friend")
    print(" 3-Add, delete, search, and update a group")
    print(" 4-GENERATE REPORTS")
    print(" 5-EXIT")
    print("-------------------------------")

def expenseMenu():
    while True:
        print("-------------------------------")
        print(" ADD/DELETE/SEARCH/UPDATE AN EXPENSE")
        print(" 1-Add an expense")
        print(" 2-Delete an expense")
        print(" 3-Search an expense")
        print(" 4-Update an expense")
        print(" 5-Go back to main menu")
        print("-------------------------------")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            # Add an expense
            pass
        elif choice == 2:
            # Delete an expense
            pass
        elif choice == 3:
            # Search an expense
            pass
        elif choice == 4:
            # Update an expense
            pass
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

def friendMenu():
    while True:
        print("-------------------------------")
        print(" ADD/DELETE/SEARCH/UPDATE A FRIEND")
        print(" 1-Add a friend")
        print(" 2-Delete a friend")
        print(" 3-Search a friend")
        print(" 4-Update a friend")
        print(" 5-Go back to main menu")
        print("-------------------------------")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            # Add a friend
            pass
        elif choice == 2:
            # Delete a friend
            pass
        elif choice == 3:
            # Search a friend
            pass
        elif choice == 4:
            # Update a friend
            pass
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

def groupMenu():
    while True:
        print("-------------------------------")
        print(" ADD/DELETE/SEARCH/UPDATE A GROUP")
        print(" 1-Add a group")
        print(" 2-Delete a group")
        print(" 3-Search a group")
        print(" 4-Update a group")
        print(" 5-Go back to main menu")
        print("-------------------------------")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            # Add a group
            pass
        elif choice == 2:
            # Delete a group
            pass
        elif choice == 3:
            # Search a group
            pass
        elif choice == 4:
            # Update a group
            pass
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

def viewLogs():
    while True:
        print("-------------------------------")
        print(" VIEW LOGS")
        print(" 1-Add a log")
        print(" 2-Delete a log")
        print(" 3-Search a log")
        print(" 4-Update a log")
        print(" 5-Go back to main menu")
        print("-------------------------------")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            # Add a log
            pass
        elif choice == 2:
            # Delete a log
            pass
        elif choice == 3:
            # Search a log
            pass
        elif choice == 4:
            # Update a log
            pass
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

while True:
    print_menu()  
    index = int(input("Enter your choice: "))

    if index == 1:
        expenseMenu()
    elif index == 2:
        friendMenu()
    elif index == 3:
        groupMenu()
    elif index == 4:
        viewLogs() 
    elif index == 5:
        print("Goodbye")
        break
