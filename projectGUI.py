from tkinter import *
from PIL import ImageTk,Image
import time
import random

root = Tk()
root.title('Eco-Life')
root.geometry("500x600")

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    timeZone = time.strftime("%Z")
    day = time.strftime("%a")
    date = time.strftime("%d")
    month = time.strftime("%b")
    year = time.strftime("%Y")

    timeLabel.config(text = hour + ":" + minute + ":" + second + " EST")
    timeLabel.after(1000, clock)

    dateLbl.config(text= day + ", " + date + " " + month + ", " + year)

myImg = ImageTk.PhotoImage(Image.open("environment.jpg"))
myLabel = Label(image = myImg, width = 200, height = 100)
#print(root.winfo_width())
myLabel.place(x=150,y=0)

timeLabel = Label(root, text="")
timeLabel.place(x=400, y=0, width=100,height=15)

dateLbl = Label(root, text="")
dateLbl.place(x=400, y=20, width=100,height=15)

clock()

welcome = Label(text="Welcome message")
welcome.place(x=175, y=40, width=150,height=15)

tipTitle = Label(text="General Lifestyle")
tipTitle.place(x=200, y=125)

tip = Label(text="Here is you random tip")
tip.place(x=95, y=150, width=150,height=15)

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

    randomTip = tipsList[random.randint(0, len(tipsList)-1)]
    tip = Label(text=randomTip)
    tip.place(x=0, y=150, width=500, height=15)

tipButton = Button(text="Generate random tip", command = generateTip)
tipButton.place(x=175, y=170)

commuteTitle = Label(text="Commuting")
commuteTitle.place(x=200, y=210)

commute = Label(text="How do you commute?")
commute.place(x=25, y=235)

carButton = Button(text="Car")
carButton.place(x=160, y=235)

transitButton = Button(text="Public transit")
transitButton.place(x=200, y=235)

walkButton = Button(text="Walk")
walkButton.place(x=300, y=235)

bikeButton = Button(text="Bike")
bikeButton.place(x=350, y=235)

carPoolButton = Button(text="Car Pool")
carPoolButton.place(x=400, y=235)

commuteMsg = Label(text="Our Recommendation")
commuteMsg.place(x=180, y=270)

plantTitle = Label(text="Your Ecosystem")
plantTitle.place(x=180, y=310)

plant = Label(text="Your plants preferences:")
plant.place(x=15, y=335)

plantOpt1 = Button(text="Exterior")
plantOpt1.place(x=145, y=335)

plantOpt2 = Button(text="Interior")
plantOpt2.place(x=200, y=335)

plantOpt3 = Button(text="Flowers")
plantOpt3.place(x=260, y=335)

bikeButton = Button(text="Fruits/vegetables")
bikeButton.place(x=320, y=335)

carPoolButton = Button(text="Low-water ")
carPoolButton.place(x=430, y=335)

commuteMsg = Label(text="Our Recommendations")
commuteMsg.place(x=180, y=370)

watering = Label(text="Next Watering time: ")
watering.place(x=15, y=395)

plantCare = Label(text="Other plant care info: ")
plantCare.place(x=250, y=395)

other = Label(text="Other Information")
other.place(x=180, y=420)

garbage = Label(text="Waste pick-up schedule: This week is Garbage/Recycling pick-up.")
garbage.place(x=40, y=440)

community = Label(text="Next up-coming community-event: Most events have been cancelled due to the restrictions")
community.place(x=20, y=460)

btn = Button(root, text="Exit Program", command = root.quit)
btn.place(x=175, y=570)

root.mainloop()
