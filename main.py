import time

continueLoop=True
while continueLoop==True:
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    print(hour + minute + second)

    if int(hour) == 22 and int(minute) ==30 and int(second) ==00:
        continueLoop = False