def CavernEntrance():
    decisions = ["left", "right", "up"]
    print("You find yourself at the entrance of a grotesque Cave filled with rot and decay.. Where do you go?")
    userInput = ""
    while userInput not in decisions:
        print("Options: left/right/up")
        userInput = input()
        if userInput == "left":
            Scene()
        elif userInput == "right":
            scene()
        elif userInput == "up":
            SSS()
