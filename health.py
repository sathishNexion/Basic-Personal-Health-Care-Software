#Created by G.Sathish Kumar , v0.5 


import time
from plyer import notification
from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n \n")


#a = int(input("Enter Water Time"))
#b = int(input("Enter eyes excersise Time"))
#c = int(input("Enter exercise Time"))


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 3600
    exsecs = 3900
    eyessecs = 1200

    while True:
        if time() - init_water > watersecs:
            notification.notify(

                title=" WATER NOTIFICATION  ",
                message="Sathish , Please Drink water ,\nIt is Good For Health and Have a Good Day   \U0001F600  \U0001F605  \U0001F602  \U0001F607",
                app_icon="F:\Health_software\water_icon.ico",
                timeout=20
            )

            print("Water Drinking time. Enter 'yes' to stop the alarm.")
            musiconloop('water_new.mp3', 'yes')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyessecs:
            notification.notify(

                title=" EYE EXERCISE NOTIFICATION  ",
                message="Sathish , Please Do Eye Exercise ,\nIt is Good For Health and Have a Good Day   \U0001F600  \U0001F605  \U0001F602  \U0001F607",
                app_icon="F:\Health_software\eye_icon.ico",
                timeout=20
            )
            print("Eye exercise time. Enter 'yes' to stop the alarm.")

            musiconloop('eye_exercise_new.mp3', 'yes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            notification.notify(

                title=" EXERCISE NOTIFICATION  ",
                message="Sathish , Please Do Exercise ,\nIt is Good For Health and Have a Good Day   \U0001F600  \U0001F605  \U0001F602  \U0001F607",
                app_icon="F:\Health_software\exercise_icon.ico",
                timeout=20
            )
            print("Physical Activity Time. Enter 'yes' to stop the alarm.")
            musiconloop('exercise_new.mp3', 'yes')
            init_exercise = time()
            log_now("Physical Activity done at")
