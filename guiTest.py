from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Eco-Life')

my_img = ImageTk.PhotoImage(Image.open("environment.jpg"))
my_label = Label(image = my_img)
my_label.pack()

btn = Button(root, text="Exit Program", command = root.quit)
btn.pack()

root.mainloop()