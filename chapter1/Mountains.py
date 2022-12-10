Axe = True
Axe = False
Axe = 30
Shield = True
Shield = False
Shield = 20
Gold = True
Gold = False
Gold = 100
Info = True
Info = False


def MountainScene():
    directions = ["forward"]
    print("You walk carefully into the misty haze of the Mountains and find a cave.. There is only one way to go..")
    userInput = ""
    while userInput not in directions:
        print("Options: forward")
        userInput = input()
        if userInput == "forward":
            Dwarfs()
        else:
            print("That is not an option o Strong one.")

def Dwarfs():
    directions = ["left", "right", "forward", "backward"]
    print("You walk into a giant Dwarfish Kingdom.. It is the Kingdom of Balfur! There must be some equipment nearby.. Where do you turn?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            Shop()
        elif userInput == "right":
            Town()
        elif userInput == "forward":
            King()
        elif userInput == "backward":
            MountainScene()
        else:
            print("That is not an option o Strong one..")

def Shop():
    global Axe
    global Shield
    global Gold
    decisions = ["axe", "shield", "leave"]
    print("You come across a local Armory, it seems this Dwarf has a Shield and an Axe for sale. You have 100 forthmite on you.. Do you make a purchase?")
    userInput = ""
    while userInput not in decisions:
        print("Options: axe/shield/leave")
        userInput = input()
        if userInput == "axe":
            print(f"(This axe will cost ya {Axe} forthmite..) You agree and purchase the Axe! You return to the Kingdoms entrance..")
            Gold = int(Gold - Axe)
            print(f"You have {Gold} forthmite remaining.")
            Axe = True
            Dwarfs()
        elif userInput == "shield":
            print(f"(This shield will cost ya {Shield} forthmite..) You agree and purchase the Shield! You return to the Kingsdom entrance..")
            Gold = int(Gold - Shield)
            print(f"You have {Gold} forthmite remaining.")
            Shield = True
            Dwarfs()
        elif userInput == "leave":
            Dwarfs()
        else:
            print("That is not an option my brother.")

def Town():
    global Info
    decisions = ["talk", "leave"]
    print("You turn and come across a town field with Dwarven Villagers. Maybe that have some useful information.. What do you do?")
    userInput = ""
    while userInput not in decisions:
        print("Options: talk/leave")
        userInput = input()
        if userInput == "talk":
            print("The local Villagers are kind and they warn you of the Goblins to the south, and of the many dangerous creatures ahead if you venture deeper into the Mountain behind the throne room. You thank the Villagers, and turn back to the entrance of the Kingdom..")
            Info = True
            Dwarfs()
        elif userInput == "leave":
            Dwarfs()
        else:
            print("That is not an option o Strong one..")

def King():
    global Axe
    global Info
    global Shield
    decisions = ["move on", "talk", "leave"]
    print("You move into a large Throne room where the King of Balfur and his Royal Guards await you.. What do you do?")
    userInput = ""
    while userInput not in decisions:
        print("Options: move on/talk/leave")
        userInput = input()
        if userInput == "move on":
            if Axe is True:
                print("The King recognizes that you have a Weapon worthy of the venture.. He lets you pass.")
                Caverns()
            if Info is True:
                print("The King can see in your eyes that you are well aware of the Dangers that lay ahead. He nods and lets you pass.")
                Caverns()
            if Shield is True:
                print("The King frowns in dissapointment. He says: You can't overcome the challenges with just a shield. Come back when you are well equipped.")
                Dwarfs()
            if Shield and Axe is True:
                print("The King recognizes that you have a Weapon worthy of the venture.. He lets you pass.")
                Caverns()
            if Axe and Info is True:
                print("The King recognizes that you have a weapon and knowledge worthy of the venture.. He lets you pass.")
                Caverns()
            else:
                print("The king does not allow you to enter.")
                Dwarfs()
        if userInput == "talk":
            print("The King informs you that he cannot allow you to continue unless you have the proper provisions in order to venture deeper into the Mountains.. He says you will need an Axe or information about the local caverns in order to pass..")
            King()
        elif userInput == "leave":
            Dwarfs()
        else:
            print("That is not an option o Strong one..")

def Caverns():
    decisions = ["left", "right", "forward", "backward"]
    print("You feel the misty breeze and cool air of the Caverns.. A chill fills your spine as you progress deeper into the Mountain.. Where do you turn?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            Spiders()
        elif userInput == "right":
            Olm()
        elif userInput == "forward":
            Hausera()
        elif userInput == "backward":
            King()
        else:
            print("That is not an option o Strong one..")

def Spiders():
    global Axe
    global Info
    actions = ["fight", "observe", "flee"]
    print("You walk slowly into the Darkness.. Suddenly you feel like you can't move anymore.. You have been trapped by Webs! There are Spiders surrounding you.. What do you do?")
    userInput = ""
    while userInput not in actions:
        print("Options: fight/observe/flee")
        userInput = input()
        if userInput == "fight":
            if Axe:
                print("You draw your Axe and cut the thread that binds you, you slash at a few Spiders into pieces! Surprised by your strength, the Spiders retreat into the Darkness.. You move on to find an exit!")
                quit()
            else:
                print("You struggle to open the Webs but before you can break the Threads the Spiders overcome you.. You die.")
                quit()
        elif userInput == "observe":
            if Info:
                print("You remember one of the Villagers mentioning the Spiders.. Apparently if you stay still, they will act cautiously and not aggressively. You wait patiently and slowly untangle yourself. You feel a rock nearby and start bashing the Spiders.. Surprised by your courage, the Spiders retreat into the Darkness.. You move on to find an exit!")
                quit()
            else:
                print("You watch the Spiders intently.. Trying to see if you can find an opening. However you are too anxious to sit still and the Spiders feast upon you.. You die.")
                quit()
        elif userInput == "flee":
            if Axe:
                print("Quickly you break out of the threads with your Axe and flee..")
                Caverns()
            else:
                print("You try to break free of the threads, but they are too strong.. The spiders feast upon you.. You die.")
                quit()
        else:
            print("That is not an option o Strong one..")

def Olm():
    global Axe
    global Info
    actions = ["fight", "observe", "flee"]
    print("You walk into a dimmly lit Cavern.. The lights come from glowing Moss illuminating from the Water.. Suddenly, you hear the screech of what sounds to be a large Serpant. It stares at you with intent to kill.. What do you?")
    userInput = ""
    while userInput not in actions:
        print("Options: fight/observe/flee")
        userInput = input()
        if userInput == "fight":
            if Axe:
                print("You draw your Axe, the Serpant hisses and sprays lethal Water in your direction! You quickly dodge, and go for the Serpants neck. You swiftly chop it off and kill the Serpant.. You move on to find an exit!")
                quit()
            else:
                print("You lunge at the Serpant in an attempt to subdue it.. Unfortunately, the Serpant is too strong for you and overcomes you.. You die.")
                quit()
        elif userInput == "observe":
            if Info:
                print("You heard tales of this Serpant from the local Villagers. Apparently its name is Olm and it has been living here for centuries. You remember the Villagers mentioning that its weakness is it's impatience.. Intrigued by this, you wait for the serpant to Strike.. Olm looks at you and Screeches! He lunges at you, you dodge haven anticipated this move. Olm hits his head on a large boulder nearby. While Olm is staggered you take a large rock and bash his head in. Blood hurdles everywhere as you slay the beast. You have killed Olm.. You move on to find an exit!")
                quit()
            else:
                print("You observe the beast waiting for an opening, but before you could think of any weakness the beast subdues you and strangles you.. You die.")
                quit()
        elif userInput == "flee":
            Caverns()
        else:
            print("That is not an option o Strong one..")

def Hausera():
    global Axe
    global Info
    actions = ["fight", "observe", "flee"]
    print("You come into a large and distgusting opening filled with Dirt and what smells like Dung.. Before you can think a Ginormous worm like create appears from the depths of the earth! What do you do?")
    userInput = ""
    while userInput not in actions:
        print("Options: fight/observe/flee")
        userInput = input()
        if userInput == "fight":
            if Axe:
                print("You draw your Axe, the Giant Worm growls in hunger as it lunges at you. You easily dodge this and make 3 huge slashes to the Worms neck. You have killed the Worm.. You move on to find an exit!")
                quit()
            else:
                print("You cry out one last battle cry as you charge at the Worm. The worm quickly digs underground and enwraps you. You are consumed by the Worm.. You die.")
                quit()
        elif userInput == "observe":
            if Info:
                print("You remember the Villagers mentioning something about this Worm.. Apparently it's speicies is called (Hausera) and they are carnivorous beasts who were the original miners before Dwarfs came along. Knowing this, you think to yourself: What is more important than food to the Hausera?.. Then it comes to you, Of course! the jewels within the Mountain. Quickly, you see nearby jewels that the beasts of dug up. You sprint in jewels general direction. Enraged the Hausera digs underground and quickly appears infront of the Jewels. Pleased by this, you take a swift turn and find an exit!")
                quit()
            else:
                print("You try and observe the Worm as best as you can, but before you can think of anything the beast enwrapes you and consumes you.. You die.")
                quit()
        elif userInput == "flee":
            Caverns()
        else:
            print("That is not an option o Strong one..")

if __name__ == "__main__":
    print("You are a Warrior who has just come from Kingsforth.")
    print("You are in search of Experience in battle in order to prove yourself.")
    print("You have come to the Mountains in search of this experience.")
    print("What is your name, o Strong one?")
    name = input()
    print(f"Good luck, {name}")
    MountainScene()
