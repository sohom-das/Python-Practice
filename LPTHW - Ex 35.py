from sys import *

def gold_room():
    print("The room is full of gold! How much do you want?")

    next = int(input("> "))

    if next >=0 and next < 50:
        print("Good! you are not a greedy man.")

    else: 
        print("You greedy bustard!")




def bear_room():
    print("""
    There is a bear here
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?\n""")
    
    move_bear = False

    while True:

        if move_bear == False:
            print("""You have two choices: 
            1. take honey
            2. taunt bear""")

            next = int(input("Enter the option number: "))

            if next == 1:
                dead("The bear looks at you then slaps your face off.")
                break
        
            elif next == 2 and not move_bear:
                print("The bear has moved from the door. You can go through it now.")
                move_bear = True

            else:
                print("i got no idea what that means!")

        else:
            print("""You have two choices: 
            1. taunt bear
            2. open door""")

            next = int(input("Enter the option number: "))

            if next == 1 and move_bear:
                dead("The bear gets pissed off and chews your leg off.")
                break
            elif next == 2 and move_bear:
                gold_room()
            else:
                print("i got no idea what that means!")
            break



def cthulhu_room():
    print("""
    Here you see the evil cthulhu.
    he, it, whatever stares at you and you go insane.
    Do you flee for yout life or eat your head?""")


    next = int(input("""
    you have two option to choose:
    1. flee
    2. head
    enter the option number."""))

    if next == 1:
        start()
    elif next == 2:
        dead("well that was tasty!")
    else:
        cthulhu_room()



def dead(why):
    print(why, "Good Job!")
    exit(0)

def start():
    print("""
    you are in adark room.
    There is door to your right and left.
    which one do you take?""")


    next = input("> ")

    if next == "right":
        cthulhu_room()

    elif next == "left":
        bear_room()

    else:
        dead("you stumble around the room untill you starve.")



start()
