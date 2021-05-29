from tkinter import *

root = Tk()
root.title("weekend Classes")
root.geometry("500x300")
root.config(bg = "light green")

lab1 = Label(root, text = "Please Enter First Number", bg = "light green")
lab1.place(x=5, y=5)
txt_entry1 = Entry(root)
txt_entry1.place(x=200, y=5)

lab2 = Label(root, text = "Please Enter Second Number", bg = "light green")
lab2.place(x=5, y=50)
txt_entry2 = Entry(root)
txt_entry2.place(x=200, y=50)

myresult = StringVar()# Must be put in before textvariable
lab3 = Label(root, text = "",textvariable = myresult, width = "18", bg = "white")
lab3.place(x=150, y=100)


def addition():
    answer = int(txt_entry1.get()) + int(txt_entry2.get())
    myresult.set(answer)


def clear():
    txt_entry1.delete(0,END)
    txt_entry2.delete(0, END)
    myresult.set("")

def bye():
    root.destroy()

btn_add = Button(root, text = "add", bg = "orange", command = addition)
btn_add.place(x=50, y=150)

btn_clear = Button(root, text = "Clear", bg = "orange", command = clear)
btn_clear.place(x=150, y=150)

btn_exit = Button(root, text = "EXIT", bg = "orange", command = bye)
btn_exit.place(x=250, y=150)

root.mainloop()
