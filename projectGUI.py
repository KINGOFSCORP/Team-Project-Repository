#-----------------------------------------------------------------------------
# Name:        Eco-Life Software
# Purpose:     This is our team project
#
# Author:      Akhil Penakacherla and Parveshwara Vanapilli Nursimulu
# Created:     27-Sep-2021
# Updated:     18-Jan-2022
#-----------------------------------------------------------------------------

from tkinter import *
from PIL import ImageTk, Image
import time
import random
import tkinter.messagebox
import webbrowser

root = Tk()
root.title('Eco-Life')
root.geometry("515x600")

myImg = ImageTk.PhotoImage(Image.open("environment.jpg"))
myCanvas = Canvas(root, width=300, height=120)
myCanvas.pack(fill="none", expand=False)
myCanvas.create_image(0, 0, image=myImg, anchor="center")
myCanvas.place(x=100, y=0)

myCanvas.create_text(155, 40, text="Welcome to the Eco-Life Software", fill="black", font=("Times New Roman", 15))
myCanvas.create_text(155, 55, text="Develop a lifestyle to save Earth", fill="black", font=("Times New Roman", 10))

waterTimeH = Entry(root, width=3)
waterTimeH.place(x=150, y=415)
waterTimeH.insert(0, "06")

colon1 = Label(text="h :")
colon1.place(x=175, y=415)

waterTimeM = Entry(root, width=3)
waterTimeM.place(x=195, y=415)
waterTimeM.insert(0, "00")

colon2 = Label(text="min :")
colon2.place(x=220, y=415)

waterTimeS = Entry(root, width=3)
waterTimeS.place(x=255, y=415)
waterTimeS.insert(0, "00")


def waterNotif(hour, minute, second):
    if int(hour) == int(waterTimeH.get()) and int(minute) == int(waterTimeM.get()) and int(second) == int(
            waterTimeS.get()):
        tkinter.messagebox.showinfo("New Notification!", "Time to water your plants!")


def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    timeZone = time.strftime("%Z")
    day = time.strftime("%a")
    date = time.strftime("%d")
    month = time.strftime("%b")
    year = time.strftime("%Y")

    timeLabel.config(text=hour + ":" + minute + ":" + second + " EST")
    timeLabel.after(1000, clock)

    dateLbl.config(text=day + ", " + date + " " + month + ", " + year)

    waterNotif(hour, minute, second)


timeLabel = Label(root, text="")
timeLabel.place(x=400, y=0, width=100, height=15)

dateLbl = Label(root, text="")
dateLbl.place(x=400, y=20, width=100, height=15)

clock()

tipTitle = Label(text="General Lifestyle")
tipTitle.place(x=200, y=125)

tip = Label(text="Here is you random tip")
tip.place(x=95, y=150, width=150, height=15)


def generateTip():
    tipsList = ["Take a shower instead of using the tub", "Pick up Trash you see",
                "Turn off electrical appliances when not in use.", "Reduce, Reuse, Recycle", "Make a Rain barrel",
                "Build a micro-composter", "Plan out a whole week of meals", "Reorganize your fridge",
                "Make a solar oven out of pizza boxes", "Borrow a book from the local library instead of buying one",
                "Make a bird feeder", "Make a plant holder out of old plastic bottles",
                "Donate or sell your used clothes", "Switch off unnecessary lights",
                "When leaving the house, reduce temperature on thermostat to reduce gas consumption",
                "Use environmentally friendly products (paper/reusable bags)", "Dispose of dead batteries properly",
                "Participate in community events and awareness campaigns"]

    randomTip = tipsList[random.randint(0, len(tipsList) - 1)]
    tip = Label(text=randomTip)
    tip.place(x=0, y=150, width=500, height=15)


tipButton = Button(text="Generate random tip", command=generateTip)
tipButton.place(x=175, y=170)

commuteTitle = Label(text="Commuting")
commuteTitle.place(x=200, y=210)

commuteQ = Label(text="Distance from your house to school?")
commuteQ.place(x=60, y=235)

distance = Entry(root, width=20)
distance.place(x=270, y=235)
distance.insert(0, "0")

km = Label(text="Km")
km.place(x=375, y=235)

commute = Label(text="How do you commute?")
commute.place(x=15, y=260)

commuteMsg = Label(text="Our Recommendation", width=60)
commuteMsg.place(x=50, y=290)


def calcTime(distance, speed):
    return (distance / speed) * 60


def calcSteps(distance, steps):
    return distance * steps


def funcCar():
    km = float(distance.get())
    if 5 >= km > 0:
        output = "If you're sporty, you could try walking or biking"
        commuteMsg.config(text=output)
    elif 5 < km <= 10:
        output = "You could try taking the school bus or public transit"
        commuteMsg.config(text=output)
    elif km > 10:
        output = "You could share a ride with a neighbour or look into hybrid or electric vehicles."
        commuteMsg.config(text=output)
    else:
        commuteMsg.config(text="Please enter a value larger than 0")


def funcTransit():
    km = float(distance.get())
    if 5 >= km > 0:
        output = "If you're sporty, you could try walking or biking"
        commuteMsg.config(text=output)
    elif km > 5:
        output = "You're doing your part to save our planet!"
        commuteMsg.config(text=output)
    else:
        commuteMsg.config(text="Please enter a value larger than 0")


def funcWalk():
    km = float(distance.get())
    if 3 >= km > 0:
        output = "Way to go! You can get some fresh air while getting " + str(calcSteps(km, 1265)) + " steps in."
        commuteMsg.config(text=output)
    elif km > 3:
        output = "Aren't you tired? You could consider biking or public transit."
        commuteMsg.config(text=output)
    else:
        commuteMsg.config(text="Please enter a value larger than 0")


def funcBike():
    km = float(distance.get())
    if 5 >= km > 0:
        output = "Great choice! Additionally you get a " + str(calcTime(km, 15)) + " minute workout."
        commuteMsg.config(text=output)
    elif km > 5:
        commuteMsg.config(text="You must love biking! You could also consider e-bikes or public transit.")
    else:
        commuteMsg.config(text="Please enter a value larger than 0")


def funcCarPool():
    km = float(distance.get())
    if 5 >= km > 0:
        output = "If you're sporty, you could try walking or biking"
        commuteMsg.config(text=output)
    elif 5 < km <= 10:
        output = "You could try taking the school bus or public transit"
        commuteMsg.config(text=output)
    elif km > 10:
        output = "Green vehicles and car-pooling is a reasonable option for this distance."
        commuteMsg.config(text=output)
    else:
        commuteMsg.config(text="Please enter a value larger than 0")


carButton = Button(text="Car", command=funcCar)
carButton.place(x=150, y=260)

transitButton = Button(text="Public transit", command=funcTransit)
transitButton.place(x=185, y=260)

walkButton = Button(text="Walk", command=funcWalk)
walkButton.place(x=275, y=260)

bikeButton = Button(text="Bike", command=funcBike)
bikeButton.place(x=320, y=260)

carPoolButton = Button(text="Car-Pool/Green Vehicle", command=funcCarPool)
carPoolButton.place(x=360, y=260)

mapsGoogle = Label(text="For more accurate infromation: ")
mapsGoogle.place(x=100, y=310)

def googleMaps():
    webbrowser.open_new("https://www.google.com/maps")

googleMapsBtn = Button(text="Go to Google Maps", command = googleMaps)
googleMapsBtn.place(x=270, y=310)

plantTitle = Label(text="Your Ecosystem")
plantTitle.place(x=180, y=330)

plant = Label(text="Your plant preferences:")
plant.place(x=5, y=355)

plantMsg = Label(text="Our Recommendations")
plantMsg.place(x=80, y=390)

def funcExtPlantBtn():
    plantMsg.config(text="You could plant Hosta, Lavender or Coral Bells")

def funcIntPlantBtn():
    plantMsg.config(text="You could plant Aloe Vera, Pothos, or Spider Plants")

def funcFlowerBtn():
    plantMsg.config(text="You could plant Marigolds, Sunflowers, or Roses")

def funcFruVegBtn():
    plantMsg.config(text="You could plant  Strawberries, Lettuces, or Tomatoes")

def funcLowWaterBtn():
    plantMsg.config(text="You could plant Philodendrons, Cacti, or Snake Plants")

extPlant = Label(text="Exterior")
extPlant.place(x=145, y=355)

extPlantBtn = Button(text=" ", width=1, command=funcExtPlantBtn)
extPlantBtn.place(x=130, y=355)

intPlant = Label(text="Interior")
intPlant.place(x=210, y=355)

intPlantBtn = Button(text=" ", width=1, command=funcIntPlantBtn)
intPlantBtn.place(x=195, y=355)

flower = Label(text="Flowers")
flower.place(x=270, y=355)

flowerBtn = Button(text=" ", width=1, command=funcFlowerBtn)
flowerBtn.place(x=255, y=355)

fruVeg = Label(text="Fruits/Vegetables")
fruVeg.place(x=330, y=355)

fruVegBtn = Button(text=" ", width=1, command=funcFruVegBtn)
fruVegBtn.place(x=315, y=355)

lowWater = Label(text="Low")
lowWater.place(x=460, y=345)

lowMaint = Label(text = "Maintenance")
lowMaint.place(x=440, y=360)

lowWaterBtn = Button(text=" ", width=1, command=funcLowWaterBtn)
lowWaterBtn.place(x=425, y=355)

plantMsg = Label(text="Our Recommendations")
plantMsg.place(x=80, y=390)

def plantSearch():
    webbrowser.open_new("https://nymag.com/strategist/article/best-indoor-plants-based-on-personality.html")

searchBtn = Button(text="Search more options", command = plantSearch)
searchBtn.place(x=380, y=385)

watering = Label(text="Watering Notification :")
watering.place(x=15, y=415)

plantCare = Label(text="s (Recommended early morning)")
plantCare.place(x=280, y=415)

garbage = Label(text="Check waste pick-up schedule: ")
garbage.place(x=40, y=460)

def wastePickup():
    webbrowser.open_new("https://www.peelregion.ca/waste/calendar/")

garbageBtn = Button(text="Check Schedule", command = wastePickup)
garbageBtn.place(x=220, y=455)


community = Label(text="Next up-coming community-event: Many events are cancelled due to the covid restrictions")
community.place(x=10, y=500)

teamOrg = Label(text="Participate in awareness campaigns and  online charities: ")
teamOrg.place(x=10, y=520)

def teamTree():
    webbrowser.open_new("https://teamtrees.org/")

teamTrees = Button(text="Team Trees", command = teamTree)
teamTrees.place(x=400, y=520)

def teamSea():
    webbrowser.open_new("https://teamseas.org/")

teamSeas = Button(text="Team Seas", command = teamSea)
teamSeas.place(x=330, y=520)

btn = Button(root, text="Exit Program", command=root.quit)
btn.place(x=175, y=570)

root.mainloop()
