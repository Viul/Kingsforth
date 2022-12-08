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
    while True:
        print("Lets start with your name.")
        name = input()
        print(f"Very well {name}. Good luck.")
        Ruins()