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
                    TownSquare()
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
                MarketScene()
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
                Ruins()
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
                OldMan()
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
            Ruins()
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
            elif Info is True:
                print("The King can see in your eyes that you are well aware of the Dangers that lay ahead. He nods and lets you pass.")
                Caverns()
            elif Shield is True:
                print("The King frowns in dissapointment. He says: You can't overcome the challenges with just a shield. Come back when you are well equipped.")
                Dwarfs()
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
            Caverns()
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

info = True
info = False

def OldMan():
    decisions = ["talk", "move on", "leave"]
    print("You approach a wide opening with an Old Man sitting on a rock seemingly meditating.. What do you do?")
    userInput = ""
    while userInput not in decisions:
        print("Options: talk/move on/leave")
        userInput = input()
        if userInput == "talk":
            print("The Old Man tells you that behind him is a puzzle that reveals the secret of the ruins. He mentions that the ruins are a huge maize that you must pass to move forward. You thank the Old Man.")
            OldMan()
        elif userInput == "move on":
            SecretPuzzle()
        elif userInput == "leave":
            Rubble()
        else:
            print("That is not an option.")
            OldMan() 

def Ruins():
    decisions = ["left", "right", "forward"]
    print("You move to find stone pillars all decaying, with hints of forestation growing on top. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            Rubble()
        elif userInput == "right":
            StoneGuardian()
        elif userInput == "forward":
            print("It's a dead end.")
            Ruins()
        else:
            print("That is not an option.")
            Ruins()

def StoneGuardian():
    decisions = ["left", "right", "forward"]
    print("You stumble across a huge statue of what looks to be a Guardian. This statue must have been important to the people that lived here.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            Ruins()
        elif userInput == "right":
            StoneGoblin()
        elif userInput == "forward":
            Temple()
        else:
            print("That is not an option.")
            StoneGuardian()
             
def StoneGoblin():
    decisions = ["left", "right", "forward", "backward"]
    print("You approach a statue that is quite different.. It seems to be a statue of an ancient Goblin Priest. There were multiple races that lived here it seems.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            StoneGuardian()
        elif userInput == "right":
            print("This is a dead end..")
            StoneGoblin()
        elif userInput == "forward":
            Library()
        elif userInput == "backward":
            print("This is a dead end.")
            StoneGoblin()
        else:
            print("That is not an option.")
            StoneGoblin()

def Rubble():
    decisions = ["left", "right", "forward", "backward"]
    print("You find piles or rubble all around you.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            print("It's a dead end.")
            Rubble()
        elif userInput == "right":
            Ruins()
        elif userInput == "forward":
            print("It's a dead end..")
            Rubble()
        elif userInput == "backward":
            OldMan()
        else:
            print("That isn't an option.")
            Rubble()

def SecretPuzzle():
    decisions = ["Goblin", "Guardian"]
    print("You come across a circular structure. A low voice starts to speak: You may choose Goblin or Guardian. Which do you choose?")
    userInput = ""
    while userInput not in decisions:
        print("Options: Goblin/Guardian")
        userInput = input()
        if userInput == "Goblin":
            Goblin1()
        elif userInput == "Guardian":
            Guardian1()
        else:
            print("That is not an option.")

def Goblin1():
    decisions = ["left", "right", "forward"]
    print("A low voice echos in the air: You have chosen Goblin. Be warned if you choose the wrong way you will be sent back to the beginning.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        elif userInput == "right":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        elif userInput == "forward":
            print("You move on..")
            Goblin2()
        else:
            print("That is not an option.")
            Goblin1()

def Goblin2():
    decisions = ["left", "right", "forward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        elif userInput == "right":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        elif userInput == "forward":
            print("You move on..")
            Goblin3()
        else:
            print("That is not an option.")
            Goblin2()

def Goblin3():
    decisions = ["left", "right", "forward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        elif userInput == "right":
            print("You move on..")
            Goblin4()
        elif userInput == "forward":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        else:
            print("That is not an option.")
            Goblin3()

def Goblin4():
    decisions = ["left", "right", "forward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        elif userInput == "right":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        elif userInput == "forward":
            print("You move on..")
            Goblin5()
        else:
            print("That is not an option.")
            Goblin4()
d
def Goblin5():
    decisions = ["left", "right", "forward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("You move on..")
            Goblin6()
        elif userInput == "right":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        elif userInput == "forward":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        else:
            print("That is not an option.")
            Goblin5()

def Goblin6():
    decisions = ["left", "right", "forward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("You move on..")
            Goblin7()
        elif userInput == "right":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        elif userInput == "forward":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        else:
            print("That is not an option.")
            Goblin6()

def Goblin7():
    decisions = ["left", "right", "forward", "backward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        elif userInput == "right":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        elif userInput == "forward":
            print("Deadend... You are thrown back to the beginning of the puzzle..")
            Goblin1()
        elif userInput == "backward":
            print("You move on..")
            Goblin8()
        else:
            print("That is not an option.")
            Goblin7()

def Goblin8():
    decisions = ["left", "right", "forward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        elif userInput == "right":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        elif userInput == "forward":
            print("You move on..")
            Goblin9()
        else:
            print("That is not an option.")
            Goblin8()

def Goblin9():
    decisions = ["left", "right", "forward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("A low voice grumbles: You have succeded in passing this test. The key to the Maze starting from Goblin is FFFRFLLBLL. Good luck. Confused, you leave.")
            OldMan()
        elif userInput == "right":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        elif userInput == "forward":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Goblin1()
        else:
            print("That is not an option.")
            Goblin9()

def Guardian1():
    decisions = ["left", "right", "forward"]
    print("A low voice echos in the air: You have chosen Guardian. Be warned if you choose the wrong way you will be sent back to the beginning.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "right":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "forward":
            print("You move on..")
            Guardian2()
        else:
            print("That is not an option.")

def Guardian2():
    decisions = ["left", "right", "forward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("You move on..")
            Guardian3()
        elif userInput == "right":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "forward":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        else:
            print("That is not an option.")

def Guardian3():
    decisions = ["left", "right", "forward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "right":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "forward":
            print("You move on..")
            Guardian4()
        else:
            print("That is not an option.")
            Guardian3()

def Guardian4():
    decisions = ["left", "right", "forward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "right":
            print("You move on..")
            Guardian5()
        elif userInput == "forward":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        else:
            print("That is not an option.")
            Guardian4()

def Guardian5():
    decisions = ["left", "right", "forward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "right":
            print("You move on..")
            Guardian6()
        elif userInput == "forward":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        else:
            print("That is not an option.")
            Guardian5()

def Guardian6():
    decisions = ["left", "right", "forward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "right":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "forward":
            print("You move on..")
            Guardian7()
        else:
            print("That is not an option.")
            Guardian6()

def Guardian7():
    decisions = ["left", "right", "forward", "backward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "right":
            print("You move on..")
            Guardian8()
        elif userInput == "forward":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        else:
            print("That is not an option.")
            Guardian7()

def Guardian8():
    decisions = ["left", "right", "forward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "right":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "forward":
            print("You move on..")
            Guardian9()
        else:
            print("That is not an option.")
            Guardian8()

def Guardian9():
    decisions = ["left", "right", "forward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("You move on..")
            Guardian10()
        elif userInput == "right":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "forward":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        else:
            print("That is not an option.")
            Guardian9()

def Guardian10():
    decisions = ["left", "right", "forward", "backward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            print("You move on..")
            Guardian11()
        elif userInput == "right":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "forward":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        else:
            print("That is not an option.")
            Guardian10()

def Guardian11():
    decisions = ["left", "right", "forward", "backward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "right":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "forward":
            print("Deadend... You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "backward":
            print("You move on..")
            Guardian12()
        else:
            print("That is not an option.")
            Guardian11()

def Guardian12():
    decisions = ["left", "right", "forward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("You move on..")
            Guardian13()
        elif userInput == "right":
            print("Deadend.")
            Guardian1()
        elif userInput == "forward":
            print("Deadend..")
            Guardian1()
        else:
            print("That is not an option.")

def Guardian13():
    decisions = ["left", "right", "forward"]
    print("Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward")
        userInput = input()
        if userInput == "left":
            print("A low voice grumbles: You have succeded in passing this test. The key to the Maze starting from Guardian is FLFRRFRFLLBLL. Good luck. Confused, you leave.")
            OldMan()
        elif userInput == "right":
            print("Deadend. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        elif userInput == "forward":
            print("Deadend.. You are thrown back to the beginning of the puzzle..")
            Guardian1()
        else:
            print("That is not an option.")
            Guardian13()

def Temple():
    decisions = ["left", "right", "forward", "backward"]
    print("You walk into 4 corner pillars of Stone with a elegant foundation. In the middle there is a stone statue, mayhap a deity. This must have been a ancient Temple.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            DeadKnights()
        elif userInput == "right":
            print("You feel the sudden crunch of bones beneath your feet.. All of a sudden a group of Ancient Soldiers slash you open.. You die. ")
            quit()
        elif userInput == "forward":
            print("You walk forward and find two Trolls feasting upon human flesh.. Before you can move they grab you and consume you whole.. You die.")
            quit()
        elif userInput == "backward":
            StoneGuardian()
        else:
            print("That is not an option.")
            Temple()

def Library():
    decisions = ["left", "right", "forward", "backward"]
    print("You move into an open space that is filled with torn books.. This must have been a Library! Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            print("You walk into a group of Undead Goblins. Before you can react they tear your body apart.. You die.")
            quit()
        elif userInput == "right":
            Hut()
        elif userInput == "forward":
            Monastery()
        else:
            print("That is not an option.")
            Library()

def DeadKnights():
    decisions = ["left", "right", "forward", "backward"]
    print("You come upon a pile of decaying bones with armor around them. It seems these poor souls were once brave knights.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            print("You walk ever so slowly.. but suddenly you fall into a trap filled with spikes! You die.")
            quit()
        elif userInput == "right":
            Temple()
        elif userInput == "forward":
            Armory()
        elif userInput == "backward":
            print("You take your time as you move into more stone structures.. Before you can react something stabs you in the back! You die.")
            quit()
        else:
            print("That is not an option.")
            DeadKnights()

def Armory():
    decisions = ["left", "right", "forward", "backward"]
    print("As you stroll deeper into the ruins, you come across a old structure that has rusted swords and shields.. This must have been a Armory! Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            print("You find a strange creature lurking in the shadows.. In the sight of this creature you freeze in horror. It cuts your throat. You die. ")
            quit()
        elif userInput == "right":
            AncientAnimal()
        elif userInput == "forward":
            print("Walking on, you creep into a brush of grass. Four goblins take you by the legs and cut you open.. You die.")
            quit()
        elif userInput == "backward":
            DeadKnights()
        else:
            print("That is not an option.")
            Armory()

def AncientAnimal():
    decisions = ["left", "right", "forward", "backward"]
    print("You walk into a plane of wildlife.. There is a majestic stallion standing right in front of you.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            Armory()
        elif userInput == "right":
            Monastery()
        elif userInput == "forward":
            print("An ancient creature appears from the depths of the wildlife. It tackles you and starts to consume your flesh.. You die. ")
            quit()
        elif userInput == "backward":
            print("As you trek the ancient wildlife, you come in contact with a group of old Soldiers. They don't seem to care for your presence, as they stand motionlessly. You walk carefully into their presence.. All at once parasites burst from their bodies and crawl into your brain.. You die. ")
            quit()
        else:
            print("That is not an option.")
            AncientAnimal()

def Hut():
    decisions = ["left", "right", "forward", "backward"]
    print("You walk into an opening with an Old Hut that's decaying.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            Library()
        elif userInput == "right":
            print("Uncomfortable with your surroundings darkness seems to surround you. A dark demon enters your brain. You perish from the darkness that consumes your mind.. You die.")
            quit()
        elif userInput == "forward":
            GoblinPriest()
        elif userInput == "backward":
            print("Confused by your surroundings you cannot find your way back. You are driven mad by this and start to scream. Eerie creatures hear your cries and consume you.. You die.")
            quit()
        else:
            print("That is not an option.")
            Hut()

def GoblinPriest():
    decisions = ["talk", "leave"]
    print("You move into an opening with a grotesque Goblin in the center. He seems to be some kind of Priest.. What do you do?")
    userInput = ""
    while userInput not in decisions:
        print("Options: talk/leave")
        userInput = input()
        if userInput == "talk":
            print("The ancient priest looks at you intently.. He speaks with an ancient tone: You have come into a a place of knowledge and despair. The deeper you travel, the more you will suffer. But, from your suffering you will gain the world. Perplexed, you thank the priest and leave.")
            Hut()
        elif userInput == "leave":
            Hut()
        else:
            print("That is not an option.")
            GoblinPriest()

def Monastery():
    decisions = ["left", "right", "forward", "backward"]
    print("You tred carefully into a large building that seems to be a ancient Monastery.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            AncientAnimal()
        elif userInput == "right":
            print("You walk into a room filled with blood. It seems there were many sacrifices here.. All of sudden, you feel the blood from your neck flowing onto the floor. You have been cut opon.. You die.")
            quit()
        elif userInput == "forward":
            Mist()
        elif userInput == "backward":
            Library()
        else:
            print("That is not an option.")
            Monastery()

def Mist():
    decisions = ["left", "right", "forward", "backward"]
    print("You wander into a deep mist that doesn't seem to have an end.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            print("Goblins appear from the brush and slice you open.. You die.")
            quit()
        elif userInput == "right":
            StrangeFigure()
        elif userInput == "forward":
            print("A large force of Mercernaries storm you. You decapitated.. You die.")
            quit()
        elif userInput == "backward":
            Monastery()
        else:
            print("That is not an option.")
            Mist()

def StrangeFigure():
    decisions = ["left", "right", "forward", "backward"]
    print("You stroll onward into the presence of a strange figure. It motionlessly stares at you.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            Mist()
        elif userInput == "right":
            print("You move into a large camp occupied by Goblins. They charge you immedietly and crush your skull.. You die.")
            quit()
        elif userInput == "forward":
            Statue()
        elif userInput == "backward":
            print("You proceed feeling the presence of dark entities. Before you can react, dark entities enter your body and force you to kill yourself.. You die.")
            quit()
        else:
            print("That is not an option.")
            StrangeFigure()

def Statue():
    decisions = ["left", "right", "forward", "backward"]
    print("A large statue comes into view. It's a statue of some ancient deity. It is so beautiful.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            Boat()
        elif userInput == "right":
            print("You are overcome by a group of cultist worshippers.. You die.")
            quit()
        elif userInput == "forward":
            print("You are overcome by a group of cultist worshippers. You die.")
            quit()
        elif userInput == "backward":
            StrangeFigure()
        else:
            print("That is not an option.")
            Statue()

def Boat():
    decisions = ["left", "right", "forward", "backward"]
    print("You find a boat sitting in the middle of nowhere. It seems that this area was once a lake.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            Desert()
        elif userInput == "right":
            Statue()
        elif userInput == "forward":
            print("You trek rough terrain, suddenly strange sea creatures appear from the distance and take you as a sacrifice.. You die.")
            quit()
        elif userInput == "backward":
            print("You trek rough terrain, suddenly strange sea creatures appear from the distance and take you as a sacrifice. You die.")
            quit()
        else:
            print("That is not an option.")
            Boat()

def Desert():
    decisions = ["left", "right", "forward", "backward"]
    print("You find yourself in a hot and arrid desert. You groan, frustrated with the circumstances.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            print("You are immedietly cornered by large desert snakes, they consume you in an instant.. You die.")
            quit()
        elif userInput == "right":
            Boat()
        elif userInput == "forward":
            print("You walk into a pit of scorpions, they stab you with lethal poison. You skin slowly turns to mush.. You die.")
            quit()
        elif userInput == "backward":
            Lake()
        else:
            print("That is not an option.")
            Desert()

def Lake():
    decisions = ["left", "right", "forward", "backward"]
    print("Finally, a body of water appears before you. This must be near the end of the journey. You take a nearby boat and begin to traverse the water.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/forward/backward")
        userInput = input()
        if userInput == "left":
            Gates()
        elif userInput == "right":
            print("You row ever so cautiously. Suddenly, a group of sirens appear from the sky and seduce you.. You die.")
            quit()
        elif userInput == "forward":
            Desert()
        elif userInput == "backward":
            print("You traverse the water with ease. Without warning, a party of ancient sharks surround your boat and eat you.. You die.")
            quit()
        else:
            print("That is not an option.")
            Lake()

def Gates():
    global info
    actions = ["chant", "pray", "attack", "move on"]
    print("A large set of Gates stand in your way. These gates seem to be made of ancient marble and beautifully sculpted gems. What do you do?")
    userInput = ""
    while userInput not in actions:
        print("Options: chant/pray/attack/move on")
        userInput = input()
        if userInput == "chant":
            if info:
                print("You chant the ancient scripture that the Goblin and Guardian taught you: In alfo Dremu con realmufa ist Afa! The Gates open! You slowly move into an infinite void..")
            else:
                print("You attempt to chant a ancient chant you learned in Kingsforth. Nothing happens..")
                Gates()
        elif userInput == "pray":
            print("You sit and clasp your hands together. You pray an ancient prayer that you were taught in Kingsforth. Nothing happens..")
            Gates()
        elif userInput == "attack":
            print("You attempt to attack the gate with your fire spell. (Morten Alma!) But, nothing happens..")
            Gates()
        elif userInput == "move on":
            GoblinandGuardian()
        else:
            print("That is not an option.")
            Gates()

def GoblinandGuardian():
    global info
    actions = ["talk", "pray", "leave"]
    print("You walk into an opening that is guarded by two ancient deity's. Both are at least 20 feet tall, made of elements you cannot recognize. What do you do?")
    userInput = ""
    while userInput not in actions:
        print("Options: talk/pray/leave")
        userInput = input()
        if userInput == "talk":
            print("You discover that both the deities are the ancient guardians of the specices that used to inhabit this land. The Goblins and Humans. They tell you that the only way to move forward beyond the gates is to chant the ancient scripture that was given in two parts to both of these deities. They recognize that you are the only one that has made it this far.. You receive the chant!")
            info = True
            GoblinandGuardian()
        elif userInput == "pray":
            print("The deities laugh at you, and say: We are not gods, we are but guardians of the Dream realm that is guarded by our Gates.")
            GoblinandGuardian()
        elif userInput == "leave":
            Gates()
        else:
            print("That is not an option.")
            GoblinandGuardian()

if __name__ == "__main__":
    print("Welcome to Kingsforth!")
    print("This is a land of opportunity.")
    print("You will find Death and Triumph as you embark on your journey..")
    print("Be warned that whoever you choose will present itself a set of challenges unique to your choice..")
    print("Let us start with your name.")
    name = input()
    print(f"Good luck, {name}")
    IntroScene()

