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

btn = Button(root, text = "Calculate", command = gen_num)
btn.place(x=130, y=140)
root.mainloop()
