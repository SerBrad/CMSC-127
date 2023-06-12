from tkinter import *
import time
from tkinter import ttk, messagebox, filedialog
import pymysql

#function 

# Function for back button
def back():
    root.destroy()
    import main

# Function for connecting to the database
def connect_database():
    def connect():
        global mycursor, con
        try:
            con = pymysql.connect(host='localhost', user='root', password='Celestial2003')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Invalid Details', parent=connectWindow)
            return
        try:
            query = 'create database transactions'
            mycursor.execute(query)
            query = 'use transactions'
            mycursor.execute(query)
            query = 'create table usergroup(groupid int AUTO_INCREMENT, groupname varchar(50) not null,groupbalance numeric(6,2),primary key(groupid))'
            mycursor.execute(query)
        except:
            query = 'use transactions'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is successful', parent=connectWindow)
        connectWindow.destroy()
        addUserButton.config(state=NORMAL)
        searchUserButton.config(state=NORMAL)
        updateUserButton.config(state=NORMAL)
        deleteUserButton.config(state=NORMAL)

    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0, 0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)

#function for top level data
def topLevel_data(title, button_text, command): 
    global idEntry, nameEntry, balanceEntry, screen
    screen=Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(0, 0)
    
    idLabel = Label(screen, text='User Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)
    
    nameLabel = Label(screen, text='User Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)
    
    balanceLabel = Label(screen, text='User Balance', font=('times new roman', 20, 'bold'))
    balanceLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    balanceEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    balanceEntry.grid(row=2, column=1, pady=15, padx=10)
    
    user_button = Button(screen, text=button_text, command=command)
    user_button.grid(row=7, columnspan=2, pady=15)
    
    if title=='Update User':
        indexing = userTable.focus()

        content = userTable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        balanceEntry.insert(0, listdata[2])

    
#function for showing all users
def show_User(): 
    query='select * from user'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    userTable.delete(*userTable.get_children())
    for data in fetched_data: 
        userTable.insert('', END, values=data)
        
#function for add_data 
def add_user(): 
    if idEntry.get()=='' or nameEntry.get()=='' or balanceEntry.get()=='': 
        messagebox.showerror('Error', 'All fields are required', parent=screen)
        
    else: 
        try: 
            query='insert into user values(%s, %s, %s)'
            mycursor.execute(query, (idEntry.get(), nameEntry.get(), balanceEntry.get()))

            con.commit()
            result=messagebox.askyesno('Confirm', 'Data added successfully. Do you want to clean the form?', parent=screen)
            if result: 
                idEntry.delete(0, END)
                nameEntry.delete(0, END)
                balanceEntry.delete(0, END)
            else: 
                pass
        except:
            messagebox.showerror('Error','Id cannot be repeated',parent=screen)
            return
            
        query='select * from user'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        userTable.delete(*userTable.get_children())
        for data in fetched_data:
            userTable.insert('',END,values=data)

#function for deleting user
def delete_user():
    indexing = userTable.focus()
    content = userTable.item(indexing)
    if 'values' in content:
        content_id = content['values'][0]
        query = 'delete from user where userid=%s'
        mycursor.execute(query, content_id)
        con.commit()
        messagebox.showinfo('Deleted', f'Id {content_id} is deleted successfully')
        show_User()
    else:
        messagebox.showerror('Error', 'No user selected.')

#function for updating user info
def update_user(): 
    query='update user set username=%s,userbalance=%s where userid=%s'
    mycursor.execute(query,(nameEntry.get(),balanceEntry.get(),idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully',parent=screen)
    screen.destroy()
    show_User()

def field_search(title, button_text, command): 
    global idEntry, screen
    screen=Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(0, 0)
    
    idLabel = Label(screen, text='User Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)
    
    user_button = Button(screen, text=button_text, command=command)
    user_button.grid(row=7, columnspan=2, pady=15) 

#function for search group
def search_user(): 
    query='select * from user where userid=%s'
    userTable.delete(*userTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        userTable.insert('',END,values=data)

# GUI part
root = Tk()
root.geometry('1174x680+0+0')
root.resizable(0, 0)
root.title('User')

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

connectButton = Button(root, text='Connect to Database', command=connect_database)
connectButton.place(x=980, y=0)

# Add user button
addUserButton = Button(leftFrame, text='Add New User', width=25,command=lambda : topLevel_data('Add New User', 'Add', add_user) )
addUserButton.grid(row=0, column=0, pady=20)

# Delete user button
deleteUserButton = Button(leftFrame, text='Delete User', width=25, command=delete_user)
deleteUserButton.grid(row=1, column=0, pady=20)

# Update user button
updateUserButton = Button(leftFrame, text='Update User', width=25, command=lambda :topLevel_data('Update User','Update',update_user))
updateUserButton.grid(row=2, column=0, pady=20)

# Search user button
searchUserButton = Button(leftFrame, text='Search User', width=25, command=lambda :field_search('Search User','Search',search_user))
searchUserButton.grid(row=3, column=0, pady=20)

# Show user button
showUserButton = Button(leftFrame, text='Show All Users', width=25, command=show_User)
showUserButton.grid(row=4, column=0, pady=20)

# Back button
backButton = Button(leftFrame, text='Back', width=25, command=back)
backButton.grid(row=5, column=0, pady=20)

rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=820, height=600)

# Group table
userTable = ttk.Treeview(rightFrame, columns=('User ID', 'User Name', 'User Balance'))
userTable.pack(expand=1, fill=BOTH)
userTable.heading('User ID', text='User ID')
userTable.heading('User Name', text='User Name')
userTable.heading('User Balance', text='User Balance')
userTable.column('User ID', width=200, anchor=CENTER)
userTable.column('User Name', width=200, anchor=CENTER)
userTable.column('User Balance', width=200, anchor=CENTER)

style = ttk.Style()
style.configure('Treeview', rowheight=40, font=('arial', 12, 'bold'), fieldbackground='white', background='white')
style.configure('Treeview.Heading', font=('arial', 14, 'bold'), foreground='red')

userTable.config(show='headings')

# clock()

root.mainloop()
