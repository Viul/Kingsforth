from variables import *
from classes import *
import logging


print(f"Welcome to Kingsforth! We are very interested to discover who you are...")

while True:
    player_class = input("Who are you? [Warrior, Mage, Theif]:")
    choose = ["Warrior", "Mage", "Theif"]
    
    if player_class == "Warrior":
        print(f"Ah.. so you are a Warrior...")
        break
    elif player_class == "Mage":
        print(f"Interesting.. so you are a Mage...")
        break
    elif player_class == "Theif":
        print(f"Oh my.. so you are a Theif...")
        break
    else:
        print("That isn't a class!")

      
name = input("What is your name?")
print(f"I see.. so you are {name} the {player_class}")

print(f"Welcome {name} to Kingsforth! In this world you will endure trials that will test your intelligence, problem solving and survival skills.")
    
while True:
    answer = input("Are you ready? [Yes, No]:")
    decision = ["Yes", "No"]

    if answer == "Yes":
        print("Very well, let your journey begin...")
        break

    elif answer == "No":
        print("Well.. that is most unfortunate.")
        
        
    else:
        print("What are you doing?!")

while True:

    if player_class == "Mage":
        print(f"Well {name}, since you are a {player_class}, you will start with these stats: {Mage}")
        break
    elif player_class == "Warrior":
        print(f"Well {name}, since you are a {player_class}, you will start with these stats: {Warrior}")
        break
    elif player_class == "Theif":
        print(f"Well {name}, since you are a {player_class}, you will start with these stats: {Theif}")
        break    
    else:
       print("I don't know at this point man..")

    while True:
        answer1 = input(f"Is this satisfactory {name}? [Yes, No]:")
        decision1 = ["Yes", "No"]

        if answer1 == "Yes":
            print(f"Very well {name} let us start your journey..")
            break
        elif answer1 == "No":
            print("I don't really know why but okay..")
            break
        else:
            print("bruh...")


        while True:

            if player_class == "Warrior":
             print (f"Chapter 1: You wake up dreary from a nights sleep at the local inn. A local prostitue lays besides you still drunk from yesterdays pleasures..")
                    
            else:
                logging.error("Error")
                    
            while True:
                warrior_answer = input(f"What do you do?:{WarriorCh1}")

                if warrior_answer == wchoice1:
                    print("She wakes up smiling happy to see you are there.. You blush ever so slightly..")
                    break
                elif warrior_answer == wchoice2:
                    print("You slowly walk out of the room and head to the bar.. There you find the inn keeper who has your massive bill from last night.")
                    break
                elif warrior_answer == wchoice3:
                    print ("You sit there contemplating your next move; (should I stand up?, should I wake her?) More thoughts than you are used to invade your mind as you drift back to sleep...")
                    break        
                else:
                    print("That isn't a choice")

