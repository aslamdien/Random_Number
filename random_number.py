from tkinter import *
import random

root = Tk()
root.title("Random Generator")
root.geometry("350x300")

result = StringVar()
lab1 = Label(root, text = "And Your Numbers Are: ")
lab1.place(x=20, y=100)
lab2 = Label(root, text = "", textvariable = result)
lab2.place(x=200, y=100)


def gen_num():
    x = 0
    mylist = []
    while x < 6:
        numbers = random.randint(1, 42)
        if numbers not in mylist:
            mylist.append(numbers)
            x = x + 1
    else:
         x = x - 1
    mylist.sort()
    result.set(mylist)

def back():
    root.destroy()
    import tkinter_challenge_random_number


btn1 = Button(root, text = "Calculate", command = gen_num)
btn1.place(x=130, y=140)
btn2 = Button(root, text = "Return To Start", command = back)
btn2.place(x=130, y=180)

root.mainloop()
