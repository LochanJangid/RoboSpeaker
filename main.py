import pyttsx3
engine = pyttsx3.init()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Lochan")
    while(True):
        x = input("Enter what you want me to speak:- ")
        if x == "q":
            engine.say('bye bye friend')
            engine.runAndWait()
            break
        command = engine.say(x)
        engine.runAndWait()
