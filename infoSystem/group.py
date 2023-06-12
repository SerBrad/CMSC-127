from tkinter import *
import time
from tkinter import ttk, messagebox, filedialog
import pymysql

# Function for clock
# def clock():
#     global date, currenttime
#     date = time.strftime('%d/%m/%Y')
#     currenttime = time.strftime('%H:%M:%S')
#     datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
#     root.after(1000, clock)

# Function for back button
def back():
    root.destroy()
    import main
    
#function for showing all groups
def show_Group(): 
    query='select * from usergroup'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    groupTable.delete(*groupTable.get_children())
    for data in fetched_data: 
        groupTable.insert('', END, values=data)

            
#function for top level data
def topLevel_data(title, button_text, command): 
    global idEntry, nameEntry, balanceEntry, screen
    screen=Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(0, 0)
    
    idLabel = Label(screen, text='Group Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)
    
    nameLabel = Label(screen, text='Group Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)
    
    balanceLabel = Label(screen, text='Group Balance', font=('times new roman', 20, 'bold'))
    balanceLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    balanceEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    balanceEntry.grid(row=2, column=1, pady=15, padx=10)
    
    group_button = Button(screen, text=button_text, command=command)
    group_button.grid(row=7, columnspan=2, pady=15)
    
    if title=='Update Group':
        indexing = groupTable.focus()

        content = groupTable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        balanceEntry.insert(0, listdata[2])

def field_search(title, button_text, command): 
    global idEntry, screen
    screen=Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(0, 0)
    
    idLabel = Label(screen, text='Group Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)
    
    group_button = Button(screen, text=button_text, command=command)
    group_button.grid(row=7, columnspan=2, pady=15) 
           
#function for add_data 
def add_group(): 
    if idEntry.get()=='' or nameEntry.get()=='' or balanceEntry.get()=='': 
        messagebox.showerror('Error', 'All fields are required', parent=screen)
        
    else: 
        try: 
            query='insert into usergroup values(%s, %s, %s)'
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
            
        query='select * from usergroup'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        groupTable.delete(*groupTable.get_children())
        for data in fetched_data:
            groupTable.insert('',END,values=data)

#function for updating group info
def update_group(): 
    query='update usergroup set groupname=%s,groupbalance=%s where groupid=%s'
    mycursor.execute(query,(nameEntry.get(),balanceEntry.get(),idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully',parent=screen)
    screen.destroy()
    show_Group()

#function for deleting group
def delete_group():
    indexing = groupTable.focus()
    content = groupTable.item(indexing)
    if 'values' in content:
        content_id = content['values'][0]
        query = 'delete from usergroup where groupid=%s'
        mycursor.execute(query, content_id)
        con.commit()
        messagebox.showinfo('Deleted', f'Id {content_id} is deleted successfully')
        show_Group()
    else:
        messagebox.showerror('Error', 'No group selected.')

#function for search group
def search_group(): 
    query='select * from usergroup where groupid=%s'
    groupTable.delete(*groupTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        groupTable.insert('',END,values=data)
        
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
        addGroupButton.config(state=NORMAL)
        searchGroupButton.config(state=NORMAL)
        updateGroupButton.config(state=NORMAL)
        deleteGroupButton.config(state=NORMAL)

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

# GUI part
root = Tk()
root.geometry('1174x680+0+0')
root.resizable(0, 0)
root.title('Group')

# datetimeLabel = Label(root, font=('times new roman', 18, 'bold'))
# datetimeLabel.place(x=5, y=5)

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

connectButton = Button(root, text='Connect to Database', command=connect_database)
connectButton.place(x=980, y=0)

# Add group button
addGroupButton = Button(leftFrame, text='Add Group', width=25, command=lambda : topLevel_data('Add Group', 'Add', add_group))
addGroupButton.grid(row=0, column=0, pady=20)

# Delete group button
deleteGroupButton = Button(leftFrame, text='Delete Group', width=25, command=delete_group)
deleteGroupButton.grid(row=1, column=0, pady=20)

# Update group button
updateGroupButton = Button(leftFrame, text='Update Group', width=25, command=lambda :topLevel_data('Update Group','Update',update_group))
updateGroupButton.grid(row=2, column=0, pady=20)

# Search group button
searchGroupButton = Button(leftFrame, text='Search Group', width=25, command=lambda :field_search('Search Group','Search',search_group))
searchGroupButton.grid(row=3, column=0, pady=20)

# Show group button
showGroupButton = Button(leftFrame, text='Show All Groups', width=25, command=show_Group)
showGroupButton.grid(row=4, column=0, pady=20)

# Back button
backButton = Button(leftFrame, text='Back', width=25, command=back)
backButton.grid(row=5, column=0, pady=20)

rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=820, height=600)

# Group table
groupTable = ttk.Treeview(rightFrame, columns=('Group ID', 'Group Name', 'Group Balance'))
groupTable.pack(expand=1, fill=BOTH)
groupTable.heading('Group ID', text='Group ID')
groupTable.heading('Group Name', text='Group Name')
groupTable.heading('Group Balance', text='Group Balance')
groupTable.column('Group ID', width=200, anchor=CENTER)
groupTable.column('Group Name', width=200, anchor=CENTER)
groupTable.column('Group Balance', width=200, anchor=CENTER)

style = ttk.Style()
style.configure('Treeview', rowheight=40, font=('arial', 12, 'bold'), fieldbackground='white', background='white')
style.configure('Treeview.Heading', font=('arial', 14, 'bold'), foreground='red')

groupTable.config(show='headings')

# clock()

root.mainloop()
