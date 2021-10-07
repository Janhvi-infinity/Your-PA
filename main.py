
import pyttsx3
import datetime
from datetime import date
#import time
text_speech = pyttsx3.init()
answer = input("What you want  :  ")
today = date.today()
today1 = str(today)


def findDay(date):
    day, month, year = (int(i) for i in today1.split('-'))
    born = datetime.date(day, month, year)

    return born.strftime("%A")


# Driver program
Day = findDay(today1)
if answer == "c":
    from datetime import datetime

    now_method = datetime.now()
    currentTime = now_method.strftime("%H")

    if Day == "Wednesday":
        if currentTime == "08":
            text_speech.say("Machine designing Tutorial is there")
            text_speech.runAndWait()
        elif currentTime == "09":
            text_speech.say("Fluid Enginearing Tutorial is there")
            text_speech.runAndWait()
        elif currentTime == "10":
            text_speech.say("S M A C A theory is there")
            text_speech.runAndWait()
        elif currentTime == "11":
            text_speech.say("A A S O M A N theory is there")
            text_speech.runAndWait()
        elif currentTime == "23" or "24":
            text_speech.say("Tharmodynamic Tutorial is there")
            text_speech.runAndWait()
        else:
            text_speech.say("ENJOY ")
            text_speech.runAndWait()



    elif Day == "Thursday":
        if currentTime == "08":
            text_speech.say("S M A C A  Lab is there")
            text_speech.runAndWait()
        elif currentTime == "09":
            text_speech.say("S M A C A  Lab is there")
            text_speech.runAndWait()

        elif currentTime == "10":
            text_speech.say("next Fluid Enginearing theory is there")
            text_speech.runAndWait()
        elif currentTime == "11":
            text_speech.say("Tharmodynamic Theory is there")
            text_speech.runAndWait()
        elif currentTime == "12":
            text_speech.say("Machine Designing Theory is there")
            text_speech.runAndWait()

        else:
            text_speech.say("ENJOY ")
            text_speech.runAndWait()

    elif Day == "Friday":
        if currentTime == "08":
            text_speech.say("Tharmo Dynamic Lab is there")
            text_speech.runAndWait()
        elif currentTime == "09":
            text_speech.say("Tharmo Dynamic Lab is there")
            text_speech.runAndWait()

        elif currentTime == "10":
            text_speech.say("Fluid Enginearing theory is there")
            text_speech.runAndWait()
        elif currentTime == "11":
            text_speech.say("A A S O M A M Theory is there")
            text_speech.runAndWait()
        elif currentTime == "12":
            text_speech.say("S M A C A Theory is there")
            text_speech.runAndWait()

        else:
            text_speech.say("ENJOY ")
            text_speech.runAndWait()


    elif Day == "Saturday":
        if currentTime == "09":
            text_speech.say("S M A C A Tutorial is there")
            text_speech.runAndWait()
        elif currentTime == "10":
            text_speech.say(" Fluid  Enginearing  Theory is there")
            text_speech.runAndWait()

        elif currentTime == "11":
            text_speech.say("Thermo Dynamic theory is there")
            text_speech.runAndWait()
        elif currentTime == "12":
            text_speech.say("Machine Design Theory is there")
            text_speech.runAndWait()
        elif currentTime == "13":
            text_speech.say(" B R A K E Brake")
            text_speech.runAndWait()
        #elif currentTime == ("14" or "15"):


        else:
            text_speech.say("ENJOY ")
            text_speech.runAndWait()
if answer == "n":
    from datetime import datetime

    now_method = datetime.now()
    currentTime = now_method.strftime("%H")

    if Day == "Wednesday":
        if currentTime == "07":
            text_speech.say("Machine designing Tutorial is there")
            text_speech.runAndWait()
        elif currentTime == "08":
            text_speech.say("Fluid Enginearing Tutorial is there")
            text_speech.runAndWait()
        elif currentTime == "09":
            text_speech.say("S M A C A theory is there")
            text_speech.runAndWait()
        elif currentTime == "10":
            text_speech.say("A A S O M A N theory is there")
            text_speech.runAndWait()
        elif currentTime == "23" or "24":
            text_speech.say("Tharmodynamic Tutorial is there")
            text_speech.runAndWait()
        else:
            text_speech.say("ENJOY ")
            text_speech.runAndWait()



    elif Day == "Thursday":
        if currentTime == "07":
            text_speech.say("S M A C A  Lab is there")
            text_speech.runAndWait()
        elif currentTime == "08":
            text_speech.say("S M A C A  Lab is there")
            text_speech.runAndWait()

        elif currentTime == "09":
            text_speech.say("Fluid Enginearing theory is there")
            text_speech.runAndWait()
        elif currentTime == "10":
            text_speech.say("Tharmodynamic Theory is there")
            text_speech.runAndWait()
        elif currentTime == "11":
            text_speech.say("Machine Designing Theory is there")
            text_speech.runAndWait()

        else:
            text_speech.say("ENJOY ")
            text_speech.runAndWait()

    elif Day == "Friday":
        if currentTime == "08":
            text_speech.say("Tharmo Dynamic Lab is there")
            text_speech.runAndWait()
        elif currentTime == "09":
            text_speech.say("Tharmo Dynamic Lab is there")
            text_speech.runAndWait()

        elif currentTime == "10":
            text_speech.say("Fluid Enginearing theory is there")
            text_speech.runAndWait()
        elif currentTime == "11":
            text_speech.say("A A S O M A M Theory is there")
            text_speech.runAndWait()
        elif currentTime == "12":
            text_speech.say("S M A C A Theory is there")
            text_speech.runAndWait()

        else:
            text_speech.say("ENJOY ")
            text_speech.runAndWait()


    elif Day == "Saturday":
        if currentTime == "09":
            text_speech.say("S M A C A Tutorial is there")
            text_speech.runAndWait()
        elif currentTime == "10":
            text_speech.say(" Fluid  Enginearing  Theory is there")
            text_speech.runAndWait()

        elif currentTime == "11":
            text_speech.say("Thermo Dynamic theory is there")
            text_speech.runAndWait()
        elif currentTime == "12":
            text_speech.say("Machine Design Theory is there")
            text_speech.runAndWait()
        elif currentTime == "13":
            text_speech.say(" B R A K E Brake")
            text_speech.runAndWait()
        #elif currentTime == ("14" or "15"):


        else:
            text_speech.say("ENJOY ")
            text_speech.runAndWait()


elif answer=="F":
    if Day == "Wednesday":
        text_speech.say(" YOU ARE FREE AT 1 PM")
        text_speech.runAndWait()
    elif Day == "Thursday":
        text_speech.say(" YOU ARE FREE AT 1 PM")
        text_speech.runAndWait()






