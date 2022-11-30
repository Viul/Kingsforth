def IntroScene():
    decisions = ["Warrior", "Mage", "Theif"]
    print("We are very interested to discover who you are..")
    userInput = ""
    while userInput not in decisions:
        print("Options: Warrior/Mage/Theif")
        userInput = input()
        if userInput == "Warrior":
            print(f"I see.. So you are a Warrior. Let your journey begin!!")
            MountainScene()
        elif userInput == "Mage":
            print(f"Interesting.. So you are a Mage. Let your journey begin!!")
            ForestScene()
        elif userInput == "Theif":
            print(f"Oh my.. So you are a Theif. Let your journey begin!!")
            DungeonScene()
        else:
            print("That is not an option.")

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
    print("Welcome to Kingsforth!")
    print("This is a land of opportunity.")
    print("You will find Death and Triumph as you embark on your journey..")
    print("Be warned that whoever you choose will present itself a set of challenges unique to your choice..")
    print("Let us start with your name.")
    name = input()
    print(f"Good luck, {name}")
    IntroScene()

