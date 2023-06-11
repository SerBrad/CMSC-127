
# 1. Add, delete, search, and update an expense;
# 2. Add, delete, search, and update a friend;
# 3. Add, delete, search, and update a group

# Reports to be generated:
# 1. View all expenses made within a month;
# 2. View all expenses made with a friend;
# 3. View all expenses made with a group;
# 4. View current balance from all expenses;
# 5. View all friends with outstanding balance;
# 6. View all groups;
# 7. View all groups with an outstanding balance

import mysql.connector

# Connect to the MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='appuser',
            password='useruser',
            database='transactions'
        )

        return connection

    except mysql.connector.Error as error:
        print("Error! Please ensure connection with database.")
        return None

def sign_up():
    connection = connect_to_database()
    cursor = connection.cursor()

    transaction_name = input("Enter your name: ")

    query = "insert into user(username, userbalance) values (%s,  0);"
    values = (transaction_name,)

    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

    print("User successfully signed up!")

def add_transaction():
    # query = "insert into transaction(transactionname, transactiondate, owedmoney, issettled, expensetype, payorid, groupid) values (%s, %s, %s, %s, "Friend Expense", 2, null);"
    return None

def delete_transaction():
    return None

def search_transaction():
    return None

def update_transaction():
    return None

def add_friend():
    return None

def delete_friend():
    return None

def search_friend():
    return None

def update_friend():
    return None

def add_group():
    return None

def delete_group():
    return None

def search_group():
    return None

def update_group():
    return None

def view_expenses_in_month():
    return None

def view_expenses_with_friend():
    return "select * from transaction natural join user_makes_transaction where userid = 1 and expenseType = \"Friend Expense\";"

def view_expenses_with_group():
    return "select * from transaction natural join user_makes_transaction where userid = 1 and expenseType = \"Group Expense\";"

def view_current_balance():
    return "select userbalance from user where userid = 1;"

def view_friends_with_outstanding_balance():
    return "select username from user join befriends on (user.userid = befriends.user1id or user.userid = befriends.user2id) and user.userid != 1 and friendbalance > 0;"

def view_all_groups():
    return "select * from usergroup;"

def view_all_groups_with_outstanding_balance():
    return "select * from usergroup where groupbalance > 0;"

def signUp():
    return None

def logIn():
    return None

def menu():
    print('''
--------------------------------------------------
1. Add transaction
2. Delete transaction
3. Search tranasaction
4. Update transaction

5. Add friend
6. Delete friend
7. Search friend
8. Update friend

9. Add group
10. Delete group
11. Search group
12. Update group

13. View all expenses made within a month;
14. View all expenses made with a friend;
15. View all expenses made with a group;
16. View current balance from all expenses;
17. View all friends with outstanding balance;
18. View all groups;
19. View all groups with an outstanding balance

0. Exit
20. Sign up
--------------------------------------------------
    ''')
# Main function to open the application and test the views
def open_application():
    menu()
    menuChoice = int(input("Enter choice: "))
    while menuChoice != 0:
        if menuChoice == 1: add_transaction()
        elif menuChoice == 2: delete_transaction()
        elif menuChoice == 3: search_transaction()
        elif menuChoice == 4: update_transaction()
        elif menuChoice == 5: add_friend()
        elif menuChoice == 6: delete_friend()
        elif menuChoice == 7: search_friend()
        elif menuChoice == 8: update_friend()
        elif menuChoice == 9: add_group()
        elif menuChoice == 10: delete_group()
        elif menuChoice == 11: search_group()
        elif menuChoice == 12: update_group()
        elif menuChoice == 13: view_expenses_in_month()
        elif menuChoice == 14: view_expenses_with_friend()
        elif menuChoice == 15: view_expenses_with_group()
        elif menuChoice == 16: view_current_balance()
        elif menuChoice == 17: view_friends_with_outstanding_balance()
        elif menuChoice == 18: view_all_groups()
        elif menuChoice == 19: view_all_groups_with_outstanding_balance()
        elif menuChoice == 20: sign_up()

        menu()
        menuChoice = int(input("Enter choice: "))

open_application()


