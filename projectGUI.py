from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Eco-Life')
root.geometry("400x400")

my_img = ImageTk.PhotoImage(Image.open("environment.jpg"))
my_label = Label(image = my_img)
my_label.pack()

hello = Label(text="Hello world!")
hello.pack()

button = Button(text="Click me!")
button.pack()

btn = Button(root, text="Exit Program", command = root.quit)
btn.pack()

root.mainloop()

