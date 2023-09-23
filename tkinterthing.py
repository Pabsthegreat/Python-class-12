from tkinter import *
import os
root=Tk()
root.geometry('300x300')

label=Label(root, text='HelloWorld')
label.pack()

def end():
    exit()

def popup():
    window=Toplevel(root)
    window.title("Exit Application")
    window.geometry("300x100")
    alert=Label(window,text="Are you sure you want to exit the application?")
    button1=Button(window,text="Yes",command=end)
    button2=Button(window,text="No")
    alert.pack()
    button1.pack(side=LEFT)
    button2.pack(side=RIGHT)
    

b=Button(root,text="Exit Application", command=popup)
b.pack()

root.mainloop()
