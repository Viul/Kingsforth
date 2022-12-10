money = 100

def SubSword(money):
    return money - 50

BuySword = SubSword(100)

weapon = True
weapon = False
market_item = True
market_item = False
royal_item = True
royal_item = False

def MarketScene():
    decisions = ["left", "right", "forward"]
    print("You find yourself in a busy Marketplace.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()   
        if userInput == "left":
            TownSquare()
        elif userInput == "right":
            Shop() 
        elif userInput == "forward":
            Town()
        else:
            print("That is not an option.")

def TownSquare():
    decisions = ["left", "right", "forward"]
    print("You find yourself in Kingsforths Town Square.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            FortuneTeller()
        elif userInput == "right":
            MarketScene()
        elif userInput == "forward":
            TownsPeople()
        else:
            print("That is not an option.")

def Shop():
    global weapon
    decisions = ["sword", "leave"]
    print(f"You come across a Shop! It seems you have {money} Forthmite. Would you like to buy anything?")
    userInput = ""
    while userInput not in decisions:
        print("Options: sword/leave")
        userInput = input()
        if userInput == "sword":
            print(f"You purchased a Sword! You have {BuySword} Forthmite left.")
            weapon = True
            MarketScene()
        elif userInput == "leave":
            MarketScene()
        else:
            print("That is not an option.")

def Town():
    decisions = ["left", "right", "forward", "backward"]
    print("You move into a eerily quiet area of the city. There seems to be no one around.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            TownsPeople()
        elif userInput == "right":
            Alley()
        elif userInput == "forward":
            Poison()
        elif userInput == "backward":
            MarketScene()
        else:
            print("That is not an option.")

def Poison():
    global market_item
    global weapon
    actions = ["fight", "flee"]
    print("You move forward into an empty area that seems to be filled with death and decay.. Suddenly, a giant poison monster emerges from depths! What do you do?")
    userInput = ""
    while userInput not in actions:
        print("Options: fight/flee")
        userInput = input()
        if userInput == "fight":
            if weapon:
                print("You draw your sword and slay the horrid creature. You survive and find a dirty Merchants Signature! You move on.")
                market_item = True
                Gates()
            else:
                print("You approach slowly trying to guage the creatures patterns. However, you are quickly swallowed by the creature and perish.. You die.")
                quit()
        elif userInput == "flee":
            Town()
        else:
            print("That is not an option.")


def Alley():
    global weapon
    actions = ["fight", "flee"]
    print("You turn into a dark alley.. You hear a slow grumble of sorts. A Giant Rat appears from the Darkness! What do you do?")
    userInput = ""
    while userInput not in actions:
        print("Options: fight/flee")
        userInput = input()
        if userInput == "fight":
            if weapon:
                print("You pull out your Ancient Sword and slay the foul beast. You turn back from the carnage..")
                Town()
                break
            else:
                print("You charge the beast, but are quickly turned into a mid day snack.. You die.")
                quit()
        elif userInput == "flee":
            Town()
        else:
            print("That is not an option")

def Inn():
    decisions = ["talk", "leave"]
    print("You come across what seems to be an Inn. There is a local bartender inside. What do you do?")
    userInput = ""
    while userInput not in decisions:
        print("Options: talk/leave")
        userInput = input()
        if userInput == "talk":
            print("You converse with the Bartender.. He tells you that to our right there is a town abandoned due to an epidemic that occured many years ago. The king decreed that no one would live there. The Bartender also inquires to tell you that the exit to the Kingdom lies only beyond the Gates. In order to pass them, you either need a Merchants Signature, or a Royal Decree. You thank the Bartender.")
            Inn()
        elif userInput == "leave":
            TownsPeople()
        else:
            print("That is not an option.")

def FortuneTeller():
    decisions = ["talk", "leave"]
    print("You turn into a strange looking tent. Inside is a Fortune Teller. She claims she can read your future.. What do you do?")
    userInput = ""
    while userInput not in decisions:
        print("Options: talk/leave")
        userInput = input()
        if userInput == "talk":
            print("The fortune teller looks at you with eyes wide.. She informs you that you will either perish with dishonor or rise to the occasion with preperation. Perplexed you move on..")
            TownSquare()
        elif userInput == "leave":
            TownSquare()
        else:
            print("That is not an option.")

def TownsPeople():
    decisions = ["left", "right", "forward", "backward"]
    print("You move into an opening filled with towns people, the busy streets of Kingsforth are beyond your imagining.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            Inn()
        elif userInput == "right":
            Town()
        elif userInput == "forward":
            Guards()
        elif userInput == "backward":
            TownSquare()
        else:
            print("That is not an option.")

def Guards():
    global weapon
    global royal_item
    decisions = ["talk", "fight", "steal", "flee"]
    print("You walk into a large court with trees around. There are guards gathered around.. It seems they are looking for you! What do you do?")
    userInput = ""
    while userInput not in decisions:
        print("Options: talk/fight/steal/flee")
        userInput = input()
        if userInput == "talk":
            print("You move slowly into the guards view and you strike a conversation. The guards look at you and realize that you are the Theif that has escaped! They murder you immedietly. You die.")
            quit()
        elif userInput == "fight":
            if weapon:
                print("You slowly move towards the guards with your weapon drawn.. You slice them down one by one. You survive and find a Royal decree! You move on from the carnage..")
                royal_item = True
                Gates()
            else:
                print("You are overcome by the Guards and perish in battle.. You die.")
                quit()
        elif userInput == "steal":
            print("You steadily creep behind one of the guards.. You find a document in his pocket.. Swiftly you take it before he notices. You have obtained a Royal Decree! You move on.")
            royal_item = True
            Gates()
        elif userInput == "flee":
            TownsPeople()
        else:
            print("That is not an option.")

def Gates():
    global market_item
    global royal_item
    decisions = ["talk", "fight", "flee"]
    print("You come across a gigantic pair of gates guarded by 100's of royal guards. What do you do?")
    userInput = ""
    while userInput not in decisions:
        print("Options: talk/fight/flee")
        userInput = input()
        if userInput == "talk":
            if market_item:
                print("You walk up to the guards and present your Merchants Signature. Reluctantly, they let you pass.. You exit!")
                quit()
            if royal_item:
                print("You walk up to the guards and present your Royal Decree. Reluctantly, they let you pass.. You exit!")
                quit()
        elif userInput == "fight":
            print("You charge forward into the chaos of men, you are swiftly struck down by 100's of arrows and spears.. You die.")
            quit()
        elif userInput == "flee":
            print("The guards notice that you are trying to make an escape. They quickly subdue you and execute you on the spot.. You die.")
            quit()
        else:
            print("That is not an option.")

if __name__ == "__main__":
    while True:
        print("You have just escaped your prison from the depths of Kingsforth.")
        print("Lets start with your name.")
        name = input()
        print(f"Good luck, {name}.")
        MarketScene()
