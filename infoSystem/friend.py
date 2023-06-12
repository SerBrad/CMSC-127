from tkinter import * 
from tkinter import ttk, messagebox, filedialog
import pymysql 

# function for back button 
def back(): 
    root.destroy()
    import main

# function for connect database
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
        addFriendButton.config(state=NORMAL)
        searchFriendButton.config(state=NORMAL)
        updateFriendButton.config(state=NORMAL)
        deleteFriendButton.config(state=NORMAL)

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
    global id1Entry, nameEntry, balanceEntry, id2Entry, screen
    screen=Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(0, 0)
    
    user1idLabel = Label(screen, text='User Id', font=('times new roman', 20, 'bold'))
    user1idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    id1Entry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    id1Entry.grid(row=0, column=1, pady=15, padx=10)
    
    nameLabel = Label(screen, text='User Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)
    
    balanceLabel = Label(screen, text='Friend Balance', font=('times new roman', 20, 'bold'))
    balanceLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    balanceEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    balanceEntry.grid(row=2, column=1, pady=15, padx=10)
    
    user2idLabel = Label(screen, text='Friend With', font=('times new roman', 20, 'bold'))
    user2idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    id2Entry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    id2Entry.grid(row=0, column=1, pady=15, padx=10)
    
    group_button = Button(screen, text=button_text, command=command)
    group_button.grid(row=7, columnspan=2, pady=15)
    
    if title=='Update Friend':
        indexing = friendTable.focus()

        content = friendTable.item(indexing)
        listdata = content['values']
        id1Entry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        balanceEntry.insert(0, listdata[2])
        id2Entry.insert(0, listdata[3])

#function for adding a friend 
def add_group(): 
    if id1Entry.get()=='' or nameEntry.get()=='' or balanceEntry.get()=='' or id2Entry.get()=='': 
        messagebox.showerror('Error', 'All fields are required', parent=screen)
        
    else: 
        try: 
            query='insert into befriends values(%s, %s, %s)'
            mycursor.execute(query, (id1Entry.get(),id2Entry.get(), nameEntry.get(), balanceEntry.get()))

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
            
        query='select * from usergroup'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        groupTable.delete(*groupTable.get_children())
        for data in fetched_data:
            groupTable.insert('',END,values=data)

    
#GUI part 
root = Tk()
root.geometry('1174x680+0+0')
root.resizable(0, 0)
root.title('Friend')

#left frame 
leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

# connect database 
connectButton = Button(root, text='Connect to Database', command=connect_database)
connectButton.place(x=980, y=0)

#add friend button
addFriendButton = Button(leftFrame, text='Add Friend', width=25)
addFriendButton.grid(row=0, column=0, pady=20)

# Delete friend button
deleteFriendButton = Button(leftFrame, text='Delete Friend', width=25)
deleteFriendButton.grid(row=1, column=0, pady=20)

# update friend button
updateFriendButton = Button(leftFrame, text='Update Friend', width=25)
updateFriendButton.grid(row=2, column=0, pady=20)

# search friend button 
searchFriendButton = Button(leftFrame, text='Search Friend', width=25)
searchFriendButton.grid(row=3, column=0, pady=20)

# show friend button 
showFriendButton = Button(leftFrame, text='Show All Friends', width=25)
showFriendButton.grid(row=4, column=0, pady=20)

# Back button
backButton = Button(leftFrame, text='Back', width=25, command=back)
backButton.grid(row=5, column=0, pady=20)

# right frame
rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=820, height=600)

# Group table
friendTable = ttk.Treeview(rightFrame, columns=('User ID', 'User Name', 'Friend Balance', 'Friend With'))
friendTable.pack(expand=1, fill=BOTH)
friendTable.heading('User ID', text='User ID')
friendTable.heading('User Name', text='User Name')
friendTable.heading('Friend Balance', text='Friend Balance')
friendTable.heading('Friend With', text='Friend With')

friendTable.column('User ID', width=200, anchor=CENTER)
friendTable.column('User Name', width=200, anchor=CENTER)
friendTable.column('Friend Balance', width=200, anchor=CENTER)
friendTable.column('Friend With', width=200, anchor=CENTER)

style = ttk.Style()
style.configure('Treeview', rowheight=40, font=('arial', 12, 'bold'), fieldbackground='white', background='white')
style.configure('Treeview.Heading', font=('arial', 14, 'bold'), foreground='red')

friendTable.config(show='headings')

root.mainloop()

