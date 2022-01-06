import tkinter as tk

window = tk.Tk()
window.title("Eco-Life")
window.geometry("300x300")

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()
button2 = tk.Button(text = "Click")

button.pack()

tk.mainloop()