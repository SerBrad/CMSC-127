from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
from tkinter import END
#functionality Part


# upon connection will add dummy values
# problem, cannot cannot display the query ressult to the screen

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

# def var_states():
#     connectWindow=Toplevel()
#     connectWindow.grab_set()
#     connectWindow.geometry('470x250+730+230')
#     connectWindow.title('Database Connection')
#     connectWindow.resizable(0,0)

#     hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
#     hostnameLabel.grid(row=0,column=0,padx=20)

#     hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
#     hostEntry.grid(row=0,column=1,padx=40,pady=20)

#     usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
#     usernameLabel.grid(row=1, column=0, padx=20)

#     usertransactiondate = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
#     usertransactiondate.grid(row=1, column=1, padx=40, pady=20)

#     passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
#     passwordLabel.grid(row=2, column=0, padx=20)

#     passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
#     passwordEntry.grid(row=2, column=1, padx=40, pady=20)

#     connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
#     connectButton.grid(row=3,columnspan=2)


#     return var1

# creates  a  text box for user input
def toplevel_data(title,button_text,command):
    global transactionid,transactionname,transactiondate,owedmoney,issettled,expensetype,payorid,groupid,screen
    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False, False)

    if(button_text=='Add'):
        # checkExpense = var_states(screen)
        
        transacID = Label(screen, text='transactionid', font=('times new roman', 20, 'bold'))
        transacID.grid(row=0, column=0, padx=30, pady=5, sticky=W)
        transactionid = Entry(screen, font=('roman', 15, 'bold'), width=24)
        transactionid.grid(row=0, column=1, pady=15, padx=10)

        transacDate = Label(screen, text='transactionname', font=('times new roman', 20, 'bold'))
        transacDate.grid(row=1, column=0, padx=30, pady=5, sticky=W)
        transactionname = Entry(screen, font=('roman', 15, 'bold'), width=24)
        transactionname.grid(row=1, column=1, pady=15, padx=10)

        transacDate = Label(screen, text='transactiondate', font=('times new roman', 20, 'bold'))
        transacDate.grid(row=2, column=0, padx=30, pady=5, sticky=W)
        transactiondate = Entry(screen, font=('roman', 15, 'bold'), width=24)
        transactiondate.grid(row=2, column=1, pady=15, padx=10)

        utang = Label(screen, text='owedemoney', font=('times new roman', 20, 'bold'))
        utang.grid(row=3, column=0, padx=30, pady=5, sticky=W)
        owedmoney = Entry(screen, font=('roman', 15, 'bold'), width=24)
        owedmoney.grid(row=3, column=1, pady=15, padx=10)

        nabayaranBaUtang = Label(screen, text='issettled', font=('times new roman', 20, 'bold'))
        nabayaranBaUtang.grid(row=4, column=0, padx=30, pady=5, sticky=W)
        issettled = Entry(screen, font=('roman', 15, 'bold'), width=24)
        issettled.grid(row=4, column=1, pady=15, padx=10)

        expenseLabel = Label(screen, text='expensetype', font=('times new roman', 20, 'bold'))
        expenseLabel.grid(row=5, column=0, padx=30, pady=5, sticky=W)
        expensetype = Entry(screen, font=('roman', 15, 'bold'), width=24)
        expensetype.grid(row=5, column=1, pady=15, padx=10)

        payorLabel = Label(screen, text='payorid', font=('times new roman', 20, 'bold'))
        payorLabel.grid(row=6, column=0, padx=30, pady=5, sticky=W)
        payorid = Entry(screen, font=('roman', 15, 'bold'), width=24)
        payorid.grid(row=6, column=1, pady=15, padx=10)
   

   

        # if(checkExpense==1):
        #     groupLabel = Label(screen, text='groupid', font=('times new roman', 20, 'bold'))
        #     groupLabel.grid(row=8, column=0, padx=30, pady=5, sticky=W)
        #     groupid = Entry(screen, font=('roman', 15, 'bold'), width=24)
        #     groupid.grid(row=8, column=1, pady=15, padx=10)
        # else:
            # groupLabel = Label(screen, text='friendid', font=('times new roman', 20, 'bold'))
            # groupLabel.grid(row=8, column=0, padx=30, pady=5, sticky=W)
            # groupid = Entry(screen, font=('roman', 15, 'bold'), width=24)
            # groupid.grid(row=8, column=1, pady=15, padx=10)

    else:
        transacID = Label(screen, text='transactionid', font=('times new roman', 20, 'bold'))
        transacID.grid(row=0, column=0, padx=30, pady=5, sticky=W)
        transactionid = Entry(screen, font=('roman', 15, 'bold'), width=24)
        transactionid.grid(row=0, column=1, pady=15, padx=10)

        transacDate = Label(screen, text='transactionname', font=('times new roman', 20, 'bold'))
        transacDate.grid(row=1, column=0, padx=30, pady=5, sticky=W)
        transactionname = Entry(screen, font=('roman', 15, 'bold'), width=24)
        transactionname.grid(row=1, column=1, pady=15, padx=10)

        transacDate = Label(screen, text='transactiondate', font=('times new roman', 20, 'bold'))
        transacDate.grid(row=2, column=0, padx=30, pady=5, sticky=W)
        transactiondate = Entry(screen, font=('roman', 15, 'bold'), width=24)
        transactiondate.grid(row=2, column=1, pady=15, padx=10)

        utang = Label(screen, text='owedemoney', font=('times new roman', 20, 'bold'))
        utang.grid(row=3, column=0, padx=30, pady=5, sticky=W)
        owedmoney = Entry(screen, font=('roman', 15, 'bold'), width=24)
        owedmoney.grid(row=3, column=1, pady=15, padx=10)

        nabayaranBaUtang = Label(screen, text='issettled', font=('times new roman', 20, 'bold'))
        nabayaranBaUtang.grid(row=4, column=0, padx=30, pady=5, sticky=W)
        issettled = Entry(screen, font=('roman', 15, 'bold'), width=24)
        issettled.grid(row=4, column=1, pady=15, padx=10)

        expenseLabel = Label(screen, text='expensetype', font=('times new roman', 20, 'bold'))
        expenseLabel.grid(row=5, column=0, padx=30, pady=5, sticky=W)
        expensetype = Entry(screen, font=('roman', 15, 'bold'), width=24)
        expensetype.grid(row=5, column=1, pady=15, padx=10)

        payorLabel = Label(screen, text='payorid', font=('times new roman', 20, 'bold'))
        payorLabel.grid(row=6, column=0, padx=30, pady=5, sticky=W)
        payorid = Entry(screen, font=('roman', 15, 'bold'), width=24)
    payorid.grid(row=6, column=1, pady=15, padx=10)
    







    execute_query = ttk.Button(screen, text=button_text, command=command)
    execute_query.grid(row=10, columnspan=2, pady=15)

# def update_transaction():



   
def show_all_transactions():
    query = 'select * from transaction'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    transactionTable.delete(*transactionTable.get_children())
    for data in fetched_data:
        transactionTable.insert('', END, values=data)



def delete_transaction():
    query='delete from transaction where transactionid=%s'
    mycursor.execute(query,payorid.get())
    con.commit()
    messagebox.showinfo('Deleted',f'Id {transactionid()} is deleted succesfully')
    query='select * from transaction'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    transactionTable.delete(*transactionTable.get_children())
    for data in fetched_data:
        transactionTable.insert('',END,values=data)


def search_transactions():
    query='select * from transaction where transactionid=%s or transactionname=%s or transactiondate=%s or owedmoney=%s or issettled=%s or expensetype=%s or payorid=%s or groupid=%s'
    mycursor.execute(query,(transactionid.get(),transactionname.get(),transactiondate.get(),owedmoney.get(),issettled.get(),expensetype.get(),payorid.get(), groupid.get()))
    transactionTable.delete(*transactionTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        transactionTable.insert('',END,values=data)

def add_transaction():
# insert into transaction(transactionid, transactionname, transactiondate, owedmoney, issettled, expensetype, payorid, groupid) values (2010, "Food", curdate(), 200, false, "Friend Expense", 2, null);
    
    if transactionid.get()=='' or transactiondate.get()=='' or transactionname.get()=='' or owedmoney.get()=='' or issettled.get()=='' or expensetype.get()=='' or payorid.get()=='' or groupid.get()=='':
        messagebox.showerror('Error','All Feilds are required',parent=screen)

    else:
        try:
            query='insert into transaction (transactionid, transactionname, transactiondate, owedmoney, issettled, expensetype, payorid, groupid) values(%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(transactionid.get(),transactionname.get(),transactiondate.get(),owedmoney.get(),issettled.get(),
                                    expensetype.get(),payorid.get(),groupid.get()))
            query ='''insert into user_makes_transaction values (1, 2010);
                        insert into user_makes_transaction values (2, 2010);
                        update user set userbalance = userbalance + 200 where userid = 1;
                        update user set userbalance = userbalance - 200 where userid = 2;
                        update befriends set friendbalance = friendbalance + 200 where user1id = 1 and user2id = 2;'''
                     
        except:
            messagebox.showerror('Error','Problem with data format',parent=screen)
            return

        query='select * from transaction;'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()    
        transactionTable.delete(*transactionTable.get_children())
        for data in fetched_data:
            transactionTable.insert('',END,values=data)




def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host='localhost',user='root',password='brad',port=3307)
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return

        try:    
            query='use transactions'
            mycursor.execute(query)
        except:
            query='use transactions'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is successful', parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)


    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usertransactiondate = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usertransactiondate.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)


def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)



#GUI Part
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('equilux')

root.geometry('1174x680+0+0')
root.resizable(0,0)
root.title('PROJECT IN CMSC 127')

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Money Management System' #s[count]=t when count is 1
sliderLabel=Label(root,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)


connectButton=ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=980,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=500)

addstudentButton=ttk.Button(leftFrame,text='Add Expense',width=25,state=DISABLED,command=lambda :toplevel_data('Add Transaction','Add',add_transaction))
addstudentButton.grid(row=1,column=0,pady=10)

searchstudentButton=ttk.Button(leftFrame,text='Search Expense',width=25,state=DISABLED,command=lambda :toplevel_data('Search Transaction','Search',search_transactions))
searchstudentButton.grid(row=2,column=0,pady=10)

deletestudentButton=ttk.Button(leftFrame,text='Delete Expense',width=25,state=DISABLED,command=delete_transaction)
deletestudentButton.grid(row=3,column=0,pady=10)
#not implemented yet
updatestudentButton=ttk.Button(leftFrame,text='Update Expense',width=25,state=DISABLED,command=lambda :toplevel_data('Update Student','Update',add_transaction))
updatestudentButton.grid(row=4,column=0,pady=10)

showstudentButton=ttk.Button(leftFrame,text='Show Expenses',width=25,state=DISABLED,command=show_all_transactions)
showstudentButton.grid(row=5,column=0,pady=10)



exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=7,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

transactionTable=ttk.Treeview(rightFrame,columns=('transactionid','transactionname','transactiondate','owedmoney','issettled','expensetype','payorid','groupid'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=transactionTable.xview)
scrollBarY.config(command=transactionTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

transactionTable.pack(expand=1,fill=BOTH)



transactionTable.heading('transactionid',text='transactionid')
transactionTable.heading('transactionname',text='transactionname')
transactionTable.heading('transactiondate',text='transactiondate')
transactionTable.heading('owedmoney',text='owedmoney')
transactionTable.heading('issettled',text='issettled')
transactionTable.heading('expensetype',text='expensetype')
transactionTable.heading('payorid',text='payorid')
transactionTable.heading('groupid',text='groupid')

transactionTable.column('transactionid',width=50,anchor=CENTER)
transactionTable.column('transactionname',width=200,anchor=CENTER)
transactionTable.column('transactiondate',width=300,anchor=CENTER)
transactionTable.column('owedmoney',width=200,anchor=CENTER)
transactionTable.column('issettled',width=300,anchor=CENTER)
transactionTable.column('expensetype',width=100,anchor=CENTER)
transactionTable.column('payorid',width=200,anchor=CENTER)
transactionTable.column('groupid',width=200,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview', rowheight=40,font=('arial', 12, 'bold'), fieldbackground='black', background='white',)
style.configure('Treeview.Heading',font=('arial', 14, 'bold'),foreground='red')

transactionTable.config(show='headings')

root.mainloop()


