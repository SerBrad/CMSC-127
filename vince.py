
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
    month = int(input("Enter month (1-12): "))
    return ("select * from transaction where month(transactiondate) = %d;", month)

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

def open_application():
    connection = connect_to_database()
    cursor = connection.cursor()

    # change this for other views
    cursor.execute(view_expenses_in_month()) 

    myresult = cursor.fetchall()
    for x in myresult:
        print(x)

    connection.commit()
    cursor.close()
    connection.close()

open_application()


