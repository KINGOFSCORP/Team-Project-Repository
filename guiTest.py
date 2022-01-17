from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Eco-Life')
root.geometry("800x500")

#bg = PhotoImage(Image.open("environment.jpg"))
bg = ImageTk.PhotoImage(Image.open("bg.png"))

my_canvas = Canvas(root, width=800, height=500)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0, 0, image=bg, anchor="nw")

root.mainloop()