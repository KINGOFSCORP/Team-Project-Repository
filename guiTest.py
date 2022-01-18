from tkinter import *

root = Tk()

root.title("Example Title ")
root.geometry('500x300')

extPlantTF = False
intPlantTF = False
flowerTF = False
fruVegTF = False
lowWaterTF = False


def funcExtPlantBtn(extPlantTF):
    extPlantTF = True


def funcIntPlantBtn(intPlantTF):
    intPlantTF = True


def funcFlowerBtn(flowerTF):
    flowerTF = True


def funcFruVegBtn(fruVegTF):
    fruVegTF = True


def funcLowWaterBtn(lowWaterTF):
    lowWaterTF = True


extPlant = Label(text="Exterior")
extPlant.pack()

extPlantBtn = Button(text=" ", width=1, command=funcExtPlantBtn(extPlantTF))
extPlantBtn.pack()

intPlant = Label(text="Interior")
intPlant.pack()

intPlantBtn = Button(text=" ", width=1, command=funcIntPlantBtn(intPlantTF))
intPlantBtn.pack()

flower = Label(text="Flowers")
flower.pack()

flowerBtn = Button(text=" ", width=1, command=funcFlowerBtn(flowerTF))
flowerBtn.pack()

fruVeg = Label(text="Fruits/Vegetables")
fruVeg.pack()

fruVegBtn = Button(text=" ", width=1, command=funcFruVegBtn(fruVegTF))
fruVegBtn.pack()

lowWater = Label(text="Low-water")
lowWater.pack()

lowWaterBtn = Button(text="✔", width=1, command=funcLowWaterBtn(lowWaterTF))
lowWaterBtn.pack()

plantMsg = Label(text="Our Recommendations")
plantMsg.pack()

if 

root.mainloop()