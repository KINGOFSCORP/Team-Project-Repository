# ----------------------------------------------------
# Name: Eco-Life sample software
# Purpose: Practice Programming by creating a simple version of the actual project
#
# Author: PVN
# Created: 27-Sep-2021
# Updated:
# ----------------------------------------------------

import random

counter = 0

print(
    'Welcome to the Eco-Life Software \nWe will give you advices on how to adapt your lifestyle to reduce your carbon foot-print!')

while counter != 1:
    # For these, we can create methods and call them to do their different tasks. I didnt do it yet

    print(
        'You can: \n1. Generate a random tip that will save the environment \n2. Determine the best way to commute to your school \n3. Set up a gardening plan \n4. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        tipsList = ["Take a shower (Do not use the tub)", "Pick up Trash you see",
                    "Turn off electrical appliances when not in use.", "Reduce, Reuse, Recycle", "Make a Rain barrel",
                    "Build a micro-composter", "Plan out a whole week of meals", "Reorganize your fridge",
                    "Make a solar oven out of pizza boxes", "Borrow a book from the local library (Instead of buying)",
                    "Make a bird feeder", "Make a plant holder out of old plastic bottles",
                    "Donate/sell your used clothes", "Switch off unnecessary lights",
                    "When leaving the house, reduce temperature on thermostat(prevent waste of furnace working for no reason)/turn off AC",
                    "Use environmentally friendly products(paper/reusable bags)", "Dispose of dead batteries properly",
                    "Participate in community events"]

        print('Here is your random tip:')
        print(tipsList[random.randint(0, len(tipsList))])

    elif choice == 2:
        print('What is the distance from your home to your school?')
        distance = int(input('Distance in kilometres: '))
        if distance <= 2:
            print('You could walk and take some fresh air every morning and afternoon')

        elif distance < 5:
            print

    elif choice == 3:
        print()

    elif choice == 4:
        print('You have chosen to exit the software')
        counter = 1

    else:
        print('Type in the correct character')