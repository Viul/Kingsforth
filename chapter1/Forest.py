Spell = True
Spell = False 
Darkbook = True
DarkBook = False

def ForestScene():
    directions = ["left", "right", "forward"]
    print("You enter the forest and find there are 3 ways to turn.. Where do you turn?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            Wolfs()
        elif userInput == "right":
            Cultist()
        elif userInput == "forward":
            Village()
        else:
            print("That is not an Option.")

def Wolfs():
    directions = ["left", "right", "forward", "backward"]
    print("You come across a pack of Wolfs! They stare at you menacingly.. Where do you go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            Puzzle()
        elif userInput == "right":
            Cubs()
        elif userInput == "forward":
            AlphaWolf()
        elif userInput == "backward":
            ForestScene()
        else:
            print("That is not an option sir..")

def Puzzle():
    global Spell
    decisions = ["forward", "backward","right", "left", "leave"]
    print("You come across a sqaure tablet with a ball in the middle. There is text at the bottom that says: (Ye who enter my dominion will have a chance to take with you my knowledge. However, if you fail you will take only death.) Hmmm... It seems the ball can be moved in four directions.. Where do you move the ball? ")
    userInput = ""
    while userInput not in decisions:
        print("Options:forward/backward/right/left/leave")
        userInput = input()
        if userInput == "forward":
            print("You push the ball forward. You wait for what seems to be an eternity.. Suddenly, you hear a *click* almost as if something went into place. The tablet opens and reveals the knowledge of a Flame Spell! You department, with confidence overflowing.")
            Spell = True
            Wolfs()
        elif userInput == "backward":
            print("You push the ball backward. You wait for what seems to be an eternity.. You don't hear anything because spikes impale you before you notice.. You die.")
            quit()
        elif userInput == "left":
            print("You push the ball to the left. You wait for what seems to be an eternity.. You don't hear anything because spikes impale you before you notice.. You die.")
            quit()
        elif userInput == "right":
            print("You push the ball to the right. You wait for what seems to be an eternity.. Suddenly, you hear a *click* almost as if something went into place. The tablet opens and reveals a toy Monkey, who starts laughing at you..")
            Puzzle()
        elif userInput == "leave":
            Wolfs()
        else:
            print("I think we have been over this man, you can't do that.")

def Cubs():
    global Spell
    actions = ["fight", "flee"]
    print("You come across a group of Wolf Cubs guarded by a very angry Mother.. What do you do?")
    userInput = ""
    while userInput not in actions:
        print("Options: fight/flee")
        userInput = input()
        if userInput == "fight":
            if Spell:
                print("You move forward ever so slowly.. However the Mother lunges at you in defense of her Cubs! Luckily, you know the Flame Spell and you kill her with your fire before she can reach you.. You move on to find an exit!")
                quit()
            else:
                print("You move forward ever so slowly.. However the Mother lunges at you in defense of her Cubs! She rips you apart.. You die.")
                quit()
        elif userInput == "flee":
            Wolfs()
        else:
            print("That isn't an option bruv.")

def AlphaWolf():
    global Spell
    actions = ["fight", "flee"]
    print("You find yourself inside a Den. This Den only holds one lone wolf guarding one of the exits of the forest.. The Alpha Wolf. You have heard of this wolf before, his name is Bjorn, and he is a fierce opponent.. What do you do?")
    userInput = ""
    while userInput not in actions:
        print("Options: fight/flee")
        userInput = input()
        if userInput == "fight":
            if Spell:
                print("You pull out your spell book and cast the Flame Spell, (Morten Alma!) Bjorn dodges this attack easily.. However, you notice that Bjorn may have a weak spot.. It's his stance! He seems to be putting a majority of his weight to the left. You cast one more Flame Spell, but this time aim for his right side. (Morten Alma!) As expected he dodges to the right.. Bjorn is hit by the Flame Spell. With Bjorn defeated, you exit the forest!")
                quit()
            else:
                print("You observe Bjorn carefully, knowing that you have no defense against him.. Before you come up with anything he lunges and rips your throat out.. You die.")
                quit()
        elif userInput == "flee":
            Wolfs()
        else:
            print("Dude, that ain't an option..")

def Village():
    actions = ["talk", "turn back", "move on"]
    print("You move through thick woods and find a Village! These people must know something you think. What do you do?")
    userInput = ""
    while userInput not in actions:
        print("Options: talk/turn back/move on")
        userInput = input()
        if userInput == "talk":
            print("You talk to the local Chief and discover that there are Wolfs to the left and an ancient Cult worshipping a God of Destruction to the right. Terrified and yet intrigued by this information, you thank the Cheif for the warning and move on..")
            Shrine()
        elif userInput == "turn back":
            ForestScene()
        elif userInput == "move on":
            Shrine()
        else:
            print("That isn't an option my guy.")

def Shrine():
    global DarkBook
    actions = ["worship", "read", "leave"]
    print("You move on from the Village and discover a Shrine of some kind've God. Hmm.. this must be the Villagers God.. There seems to be some text at the bottom of the Shrine. What do you do?")
    userInput = ""
    while userInput not in actions:
        print("Options: worship/read/leave")
        userInput = input()
        if userInput == "worship":
            print("You start to hear a low grumble from the depths of the Shrine.. (Ye have come to a place of Darkness.. a place that will change you forever.. You have been chosen to take this book in defiance of the God of Destruction Muthar! You receieve a mysterious Dark Book. However, you have no time to process, for you are suddenly transported to the Forest entrance..")
            DarkBook = True
            ForestScene()
        elif userInput == "read":
            print("You start to read the bottom of the Shrines text.. (The chosen one will worship here and receive a gift.. A gift to destroy the very foundation of Muthar, the God of Destruction.) Intrigued, you wonder if you should worship this shrine..")
            Shrine()
        elif userInput == "leave":
            Village()
        else:
            print("Brother.. THAT AINT AN OPTION!")

def Cultist():
    directions = ["left", "right", "forward", "backward"]
    print("You have entered into the dominion of Cultists. Ten of them are gathered around a shrine of sorts all in deep prayer. They seem to be worshiping some kind've Dark Entity.. Where do you go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            Priest()
        elif userInput == "right":
            print("You run into a Wall..")
            Cultist()
        elif userInput == "forward":
            print("You come across a group of chanting Cultists, before you can even think they take you by the arms and bind you. You are cut open and used as a sacrifice for their God.. You die.")
            quit()
        elif userInput == "backward":
            ForestScene()
        else:
            print("That is not an option. For the 15th time.")

def Priest():
    global DarkBook
    global Spell
    actions = ["vanquish", "join", "flee"]
    print("You walk into a opening with the forest. There you discover a Priest praying some kind of Demonic Prayer.. What do you do?")
    userInput = ""
    while userInput not in actions:
        print("Options: vanquish/join/flee")
        userInput = input()
        if userInput == "vanquish":
            if DarkBook:
                print("You pull out the DarkBook and start chanting.. The priest stares in horror as his body starts to melt.. You have killed the Priest! You move on.")
                Riddle()
            if Spell:
                print("You pull out your spell book and cast your fire spell. (Morten Alma!) The fire blows through the Priest and burns him to death.. You have kiled the Priest! You move on.")
                Riddle()
            else:
                print("You charge the Priest in hopes of subdueing him, he smiles at you and casts a Dark Spell. Slowly your body turns into mush.. You die.")
                quit()
        elif userInput == "join":
            print("You plead with the Priest, (Please let me join you!) The Priest looks at you in dissapointment and stabs you in the heart.. You die.")
            quit()
        elif userInput == "flee":
            Cultist()
        else:
            print("That isn't an option Bruver")

def Riddle():
    decisions = ["skull", "worm","paper"]
    print("After defeating the Priest, you find yourself in front of an Old Man.. He says you must solve a Riddle in order to escape the Forest. Here is the Riddle: (I don't have eyes, But once I did see. I once had thoughts, Now white and empty. What is the answer?")
    userInput = ""
    while userInput not in decisions:
        print("Options: skull/worm/paper")
        userInput = input()
        if userInput == "skull":
            print("The Old man giggles and says: (That is correct, wise one.) You have been let through!")
            quit()
        elif userInput == "worm":
            print("The Old Man looks disappointed, suddenly arrows come flying at you! You die.")
            quit()
        elif userInput == "paper":
            print("The Old Man laughs hysterically: (That was a good guess, but not what I seek..) You are pushed back by a gust of wind into a wall of spikes.. You die.")
            quit()
        else:
            print("That is not an option o stupid one.")

if __name__ == "__main__":
    while True:
        print("You are a Mage who has just come from the Libraries of Kingsforth.")
        print("You are seeking knowledge from nearby settlments about the world around you.")
        print("You come across a Dark Forest, where you know for sure you will find something..")
        print("What is your name, o wise one?")
        name = input()
        print(f"Good luck, {name}")
        ForestScene()
