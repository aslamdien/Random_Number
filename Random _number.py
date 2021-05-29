from tkinter import *
import random

root = Tk()
root.title("Random Generator")
root.geometry("400x400")

result = StringVar()

lab = Label(root, text = "", textvariable = result)
lab.place(x=90, y=150)


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
btn.place(x=130, y=200)
root.mainloop()
