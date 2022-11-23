from variables import *
from classes import *


print(f"Welcome to Kingsforth! We are very interested to discover who you are...")

while True:
    player_class = input("Who are you? [Warrior, Mage, Theif]:")
    choose = ["Warrior", "Mage", "Theif"]
    
    if player_class == "Warrior":
        print(f"Ah.. so you are a Warrior...")

    elif player_class == "Mage":
        print(f"Interesting.. so you are a Mage...")
   
    elif player_class == "Theif":
        print(f"Oh my.. so you are a Theif...")
    
    else:
        print("That is not a class")
        exit()

    name = input("What is your name?")
    print(f"Ah.. so you are {name} the {player_class}")

    print(f"Welcome {name} to Kingsforth! In this world you will endure trials that will test your intelligence, problem solving and survival skills.")
    
    while True:
        answer = input("Are you ready? [Yes, No]:")
        decision = ["Yes", "No"]

        if answer == "Yes":
            print("Very well, let your journey begin...")
            break

        elif answer == "No":
            print("Well.. that is most unfortunate.")
            exit()
        
        else:
            print("What are you doing?!")

    if player_class == "Mage":
        print(f"Well {name}, since you are a {player_class}, you will start with these stats: {Mage}")

    elif player_class == "Warrior":
        print(f"Well {name}, since you are a {player_class}, you will start with these stats: {Warrior}")

    elif player_class == "Theif":
        print(f"Well {name}, since you are a {player_class}, you will start with these stats: {Theif}")
        
    else:
        print("Error.")

    print(f"Forthmite is our currency in Kingsforth, you will start with $100 like anyone else. Some friendly advice {name}.. Don't spend it all in one place, you might need it later on.. We wish you luck as you fight for your survival..")

    while True:
        answer1 = input(f"Would you still like to continue {name}? [Yes, No]:")
        decision1 = ["Yes", "No"]

        if answer1 == "Yes":
            print(f"Very well {name} let us start your journey..")

        if answer1 == "No":
            print("I don't really know why but okay..")
            exit()