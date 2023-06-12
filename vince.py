
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

current_id = 1

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

    # Inputs
    user_name = input("Enter your name: ")

    # Query
    query = "insert into user(username, userbalance) values (%s,  0);"
    values = (user_name,)

    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

    print("User successfully signed up!")

def add_transaction():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        # Inputs
        transaction_id = int(input("Enter transaction id: "))
        transaction_name = input("Enter transaction name: ")
        transaction_date = input("Enter transaction date (YYYY-MM-DD): ")
        owed_money = float(input("Enter owed money: "))
        is_settled = bool(input("Is the transaction settled? (True/False): "))
        expense_type = input("Enter expense type (Friend Expense / Group Expense): ")

        if expense_type == "Friend Expense":
            friend_id = input("Enter id of friend involved: ")
            group_id = None
        elif expense_type == "Group Expense":
            group_id = input("Enter id of group involved: ")

        payor_id = int(input("Enter payor ID: "))

        # Query
        query = "insert into transaction(transactionid, transactionname, transactiondate, owedmoney, issettled, expensetype, payorid, groupid) values (%s, %s, %s, %s, %s, %s, %s, %s);"
        values = (transaction_id, transaction_name, transaction_date, owed_money, is_settled, expense_type, payor_id, group_id)
        cursor.execute(query, values)

        if expense_type == "Friend Expense":

            query = "insert into user_makes_transaction values (%s, %s);"
            values = (current_id, transaction_id)
            cursor.execute(query, values)

            query = "insert into user_makes_transaction values (%s, %s);"
            values = (friend_id, transaction_id)
            cursor.execute(query, values)


        elif expense_type == "Group Expense":
            query = "select userid from joins where groupid = %s;"
            cursor.execute(query, (group_id,))
            group_members = cursor.fetchall()
            num = len(group_members)
            owed_money_per_member = owed_money / num

            # Insert all group members into user_makes_transaction
            query = "insert into user_makes_transaction values (%s, %s);"
            for member in group_members:
                values = (member[0], transaction_id)
                cursor.execute(query, values)

            # Update userbalance for each member
            query = "UPDATE user SET userbalance = userbalance - %s WHERE userid = %s;"
            for member in group_members:
                values = (owed_money_per_member, member[0])
                cursor.execute(query, values)

        

        # query = "insert into transaction(transactionname, transactiondate, owedmoney, issettled, expensetype, payorid, groupid) values (%s, %s, %s, %s, %s, %s, %s);"
        # values = (transaction_name, transaction_date, owed_money, is_settled, expense_type, payor_id, group_id)
        # cursor.execute(query, values)

        connection.commit()
    
    except Exception:
        print("Invalid input! Please enter valid values.")

    finally:
        cursor.close()
        connection.close()

def delete_transaction():
    return None

def search_transaction():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        query = "select * from transaction;"

        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            print("Transactions found:")
            for row in result:
                print(row)
        else:
            print("No transactions found.")

    except Exception:
        print("Invalid input! Please enter valid values.")

    finally:
        cursor.close()
        connection.close()

def update_transaction():
    return None

def add_friend():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        friend_id = input("Enter id of new friend: ")
        query = "insert into befriends values (%s, %s, 0);"
        values = (current_id, friend_id)

        cursor.execute(query, values)
        connection.commit()
        print("Friend successfully added!")

    except Exception:
        print("Invalid input! Please enter valid values.")

    finally:
        cursor.close()
        connection.close()

def delete_friend():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        friend_id = input("Enter id of to be deleted friend: ")
        query = "delete from befriends where (user1id = %s and user2id = %s) or (user1id = %s and user2id = %s);"
        values = (current_id, friend_id, friend_id, current_id)

        cursor.execute(query, values)
        connection.commit()
        print("Friend successfully deleted!")

    except Exception:
        print("Invalid input! Please enter valid values.")

    finally:
        cursor.close()
        connection.close()

def search_friend():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        query = "select userid, username from user join befriends on (user.userid = befriends.user1id or user.userid = befriends.user2id) and user.userid != %s;"
        values = (current_id,)

        cursor.execute(query, values)
        result = cursor.fetchall()

        if result:
            print("Friends found:")
            for row in result:
                print(row)
        else:
            print("No friends found.")

    except Exception:
        print("Invalid input! Please enter valid values.")

    finally:
        cursor.close()
        connection.close()

def update_friend():
    return None

# ----- Add group -----
# insert into joins values(3,3);
# ----- Delete group -----
# delete from joins where userid = 1 and groupid = 1;
# ----- Search group -----
# select * from usergroup;
# ----- Update group -----
# update usergroup set groupname = "Arianators" where groupname = "Swifties"; -- updates necessary values set by logged in user (ex: groupname)

def add_group():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        group_id = input("Enter group id to join: ")
        query = "insert into joins values(%s,%s)"
        values = (current_id, group_id)

        cursor.execute(query, values)
        connection.commit()
        print("Successfully joined group!")

    except Exception:
        print("Invalid input! Please enter valid values.")

    finally:
        cursor.close()
        connection.close()

def delete_group():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        group_id = input("Enter group id to unjoin: ")
        query = "delete from joins where userid = %s and groupid = %s"
        values = (current_id, group_id)

        cursor.execute(query, values)
        connection.commit()
        print("Successfully unjoined group!")

    except Exception:
        print("Invalid input! Please enter valid values.")

    finally:
        cursor.close()
        connection.close()

def search_group():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        query = "select * from usergroup;"

        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            print("Groups found:")
            for row in result:
                print(row)
        else:
            print("No groups found.")

    except Exception:
        print("Invalid input! Please enter valid values.")

    finally:
        cursor.close()
        connection.close()

def update_group():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        return None

    except Exception:
        print("Invalid input! Please enter valid values.")

    finally:
        cursor.close()
        connection.close()

def view_expenses_in_month():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        month = int(input("Enter month (1-12): "))

        query = "select * from transaction where month(transactiondate) = %s"
        values = (month,)

        cursor.execute(query, values)
        result = cursor.fetchall()

        if result:
            print("Expenses made within the month:")
            for row in result:
                print(row)
        else:
            print("No expenses found for the month.")

    except Exception:
        print("Invalid input! Please enter valid values.")

    finally:
        cursor.close()
        connection.close()

def view_expenses_with_friend():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        query = "select * from transaction natural join user_makes_transaction where userid = %s or userid = 2 and expenseType = \"Friend Expense\";"
        values = (current_id,)

        cursor.execute(query, values)
        result = cursor.fetchall()

        if result:
            print("Expenses made with friends:")
            for row in result:
                print(row)
        else:
            print("No expenses found with friends.")

    except Exception:
        print("Invalid input! Please enter valid values.")

    finally:
        cursor.close()
        connection.close()
    
    return "select * from transaction natural join user_makes_transaction where userid = 1 and expenseType = \"Friend Expense\";"

def view_expenses_with_group():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        return None

    except Exception:
        print("Invalid input! Please enter valid values.")

    finally:
        cursor.close()
        connection.close()

def view_current_balance():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        query = "select userbalance from user where userid = %s"
        values = (current_id,)

        cursor.execute(query, values)
        result = cursor.fetchone()

        print("Current balance:", result[0])

    except Exception:
        print("Invalid input! Please enter valid values.")

    finally:
        cursor.close()
        connection.close()

def view_friends_with_outstanding_balance():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        query = "select userid, username, userbalance from user join befriends on (user.userid = befriends.user1id or user.userid = befriends.user2id) and user.userid != %s and friendbalance > 0;"
        values = (current_id,)

        cursor.execute(query, values)
        result = cursor.fetchall()

        if result:
            print("Friends with outstanding balance:")
            for row in result:
                print(row[0])
        else:
            print("No friends found with outstanding balance.")

    except Exception:
        print("Invalid input! Please enter valid values.")

    finally:
        cursor.close()
        connection.close()

def view_all_groups():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        query = "select * from usergroup;"
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            print("All groups:")
            for row in result:
                print(row)
        else:
            print("No groups found.")

    except Exception:
        print("Invalid input! Please enter valid values.")

    finally:
        cursor.close()
        connection.close()

def view_all_groups_with_outstanding_balance():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        query = "select * from usergroup where groupbalance > 0;"

        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            print("Groups with outstanding balance:")
            for row in result:
                print(row)
        else:
            print("No groups found with outstanding balance.")

    except Exception:
        print("Invalid input! Please enter valid values.")

    finally:
        cursor.close()
        connection.close()

def logIn():
    return None

def menu():
    print('''
--------------------------------------------------
        Options: 
        
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
20. Sign up
21. Log In
0. Exit
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


