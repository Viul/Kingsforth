weapon = True
weapon = False
weight = True
weight = False

def DungeonScene():
    directions = ["left", "right", "forward"]
    print("You have just escaped your cell. Where do you go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            Corpses()
        elif userInput == "right":
            Guards()
        elif userInput == "forward":
            print("You find yourself at a deadend..")
            DungeonScene()
        else:
            print("Come on man..")

def Corpses():
    directions = ["right", "backward"]
    global weapon
    print("You start to smell pungent oaders of decay and death. You have come across a room filled with corpses! Where do you go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right//backward")
        userInput = input()
        if userInput == "left":
            print("You see a sword resting on a decaying mantle.. You take it!")
            weapon = True
        elif userInput == "right":
            Goblin()
        elif userInput == "backward":
            DungeonScene()
        else:
            print("I thought we went over this man..")

def Goblin():
        actions = ["fight", "flee"]
        global weapon
        print("You see a hoard of Goblins thirsting for blood.. What do you do?")
        userInput = ""
        while userInput not in actions:
            print("Options: fight/flee")
            userInput = input()
            if userInput == "fight":
                if weapon:
                    print("You use the ancient sword to fight through the Goblins. You kill them all one by one. You survive, and find one of the exits!")
                    quit()
                else:
                    print("You are overcome by the Goblin hoard and persih..")
                quit()
            if userInput == "flee":
                Corpses()
            else:
                print("Please enter a valid option bruv..")
      
def Guards():
    actions = ["forward", "right", "left"]
    global weight
    global weapon
    print("You slowly walk into a dim-lighted 4-way Corridor. You see 2 Guards standing in the middle playing Jin.. What do you do?")
    userInput = ""
    while userInput not in actions:
        print("Options: forward/right/left")
        userInput = input()
        if userInput == "forward":
            if weapon:
                print("You slay both guards and escape!")
                quit()
            if weight:
                print("You come across the guards, but you are weighed down by the gold.. They slay you. You die.")
                quit()
            else:
                print("You are slain by the guards.. You die.")
                quit()
        elif userInput == "right":
            print("You find a room filled with treasures, since you are a Theif you can't help but take it..")
            weight = True
            Guards()
        elif userInput == "left":
            Bandits()
        else:
            print("Why dude.")

def Bandits():
    actions = ["talk","leave"]
    global weight
    print("You see a couple of Bandits imprisoned. Not so different from yourself.. What do you do?")
    userInput = ""
    while userInput not in actions:
        print("Options: talk/leave")
        userInput = input()
        if userInput == "talk":
            if weight:
                print("The bandits observe you.. They see you have gold on you, the moment you get closer they slice your throat and steal your gold.. You die.")
                quit()
            else:
                print("You find out that these bandits have suffered at the hands of Kingsforth. They were arrested for raiding a slave encampment that was owned by a Duke of Kingsforth. After hearing this you wish them luck and are on your way..")  
                Guards() 
        if userInput == "leave":
            Guards()
        else:
            print("That is not an option my brother.")

if __name__ == "__main__":
    while True:
        print("You're a Theif who has just escaped his prison cell.")
        print("You have nothing and are desperate to find a way out.")
        print("Lets start with your name")
        name = input()
        print(f"Good luck, {name}.")
        DungeonScene()
