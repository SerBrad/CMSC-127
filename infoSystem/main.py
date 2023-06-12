from tkinter import *
from PIL import Image
from PIL import ImageTk

#function 
def openGroup(): 
    root.destroy()
    import group

def exit(): 
    root.destroy()

#main 
root = Tk()
root.geometry('1174x680+80+0')

#welcome label 
welcome_Label = Label(root, text='Welcome to InfoSystem', font=('times new roman',30,'italic bold'))
welcome_Label.place(x=400, y=30)
# root.wm_attributes('-transparentcolor', root['bg'])

logo=Image.open('logo.png')
newLogo=logo.resize((200, 200))
newLogo.save('newLogo.png')

logo_Image = PhotoImage(file='newLogo.png')
logo_Label=Label(root, image=logo_Image)
logo_Label.place(x=480,y=150)

#bottom frame 
bottomFrame = Frame(root)
bottomFrame.place(x=310, y=400, width=500, height=350)

# add new user
newUserButton = Button(bottomFrame, text='New User',height=2,width=40, bg='blue')
newUserButton.grid(row=0, column=0, padx=130, pady=5)

#friend button
friendButton = Button(bottomFrame, text='Friend', height=2, width=40, bg='blue')
friendButton.grid(row=1, column=0, padx=130, pady=5)

#group button
groupButton = Button(bottomFrame, text='Group', height=2, width=40, bg='blue', command=openGroup)
groupButton.grid(row=2, column=0, padx=130, pady=5)

#expense button 
transactionButton = Button(bottomFrame, text='Transaction', height=2, width=40, bg='blue')
transactionButton.grid(row=3, column=0, padx=130, pady=5)

#expense button 
exitButton = Button(bottomFrame, text='Exit', height=2, width=40, bg='blue', command=exit)
exitButton.grid(row=4, column=0, padx=130, pady=5)

root.resizable(0, 0)
root.title('Info System')

root.mainloop()
