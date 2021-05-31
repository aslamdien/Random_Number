from tkinter import *
from tkinter import messagebox
from datetime import date

root = Tk()
root.title("How Old Are You")
root.geometry("500x500")

year = StringVar()
month = StringVar()
day = StringVar()

lab1 = Label(root, text = "Year Your Were Born:")
lab1.place(x=50, y=10)
ent1 = Entry(root, textvariable = year)
ent1.place(x=200, y=10)

lab2 = Label(root, text = "Month:")
lab2.place(x=50, y=50)
ent2 = Entry(root, textvariable = month)
ent2.place(x=200, y=50)

lab3 = Label(root, text = "Date:")
lab3.place(x=50, y=90)
ent3 = Entry(root, textvariable = day)
ent3.place(x=200, y=90)


def calculateAge():
    today = date.today()
    birthDate = date(int(year.get()), int(month.get()), int(day.get()))
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

    if age < 18:
        messagebox.showinfo("SORRY", "You Are " + str(age) + ", Too Young, Try Again In A Few Years")
        root.destroy()
        import tkinter_challenge_random_number

    if age >= 18:
        messagebox.showinfo("CONGRATULATIONS", "You Are " + str(age)+ ", You Can Enter")
        root.destroy()
        import random_number


def clear():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)


def exit():
    root.destroy()
    import tkinter_challenge_random_number

btn1 = Button(root, text = "And You Are", command = calculateAge)
btn1.place(x=50, y=150)
btn2 = Button(root, text = "Clear", command = clear)
btn2.place(x=200, y=150)
btn3 = Button(root, text = "Exit", command = exit)
btn3.place(x=300, y=150)

root.mainloop()
