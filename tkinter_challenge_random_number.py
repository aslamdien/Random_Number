# Generate 6 random numbers
# Between 1 - 40
# No Number should be repeated
# Display result in a label
# the No. should be sorted
# hint = import random to generate random numbers
from tkinter import *

root = Tk()
root.title("Username/Password")
root.geometry("500x500")

lab1 = Label(root, text = "Please Enter Your Username:")
lab1.place(x=5, y=10)
ent1 = Entry(root)
ent1.place(x=200, y=10)

lab2 = Label(root, text = "Please Enter Your Password:")
lab2.place(x=5, y=50)
ent2 = Entry(root, show = "*")
ent2.place(x=200, y=50)

username = StringVar()
password = StringVar()


def clear():
    ent1.delete(0, END)
    ent2.delete(0, END)


def verify():
    from tkinter import messagebox
    username = ["Zoe", "Lihle", "Liyaah", "Masi"]
    password = ["9595","6868", "6060", "1001"]
    found = False

    for x in range(len(username)):
        if ent1.get() == username[x] and ent2.get() == password[x]:
            found = True

    if found == True:
        messagebox.showinfo("STATUS", "Access Granted!")
        root.destroy()

    else:
        messagebox.showinfo("ERROR INFO", "Access Denied!!!")
        ent1.delete(0, END)
        ent2.delete(0, END)

btn1 = Button(root, text = "Verify", command = verify)
btn1.place(x=100, y=100)
btn2 = Button(root, text = "Clear", command = clear)
btn2.place(x=200, y=100)

root.mainloop()
