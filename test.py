# Importing module
import mysql.connector
 
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "appuser",
    password = "useruser"
)
 
# Printing the connection object
print(mydb)

if(mydb): 
    print("Connection Successful")
    mycursor = mydb.cursor()
    mycursor.execute("Show databases")
    for db in mycursor: 
        print(db)
else: 
    print("Not")
    
