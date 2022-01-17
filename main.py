from tkinter import *
import time

root = Tk()
root.title('Clock')
root.geometry("600x400")

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    timeZone = time.strftime("%Z")
    day = time.strftime("%a")
    date = time.strftime("%d")
    month = time.strftime("%b")
    year = time.strftime("%Y")

    my_label.config(text = hour + ":" + minute + ":" + second + " EST" )
    my_label.after(1000, clock)

    my_label2.config(text= day + ", " + date + " " + month + ", " + year)

my_label = Label(root, text = "")
my_label.pack()

my_label2 = Label(root, text = "")
my_label2.pack()

clock()

root.mainloop()
