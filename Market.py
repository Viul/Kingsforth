def SubSteak(money):
    return money - 7

def SubPork(money):
    return money - 5

def SubHealth(money):
    return money - 20

def SubStamina(money):
    return money - 20

BuySteak = SubSteak(100)
BuyPork = SubPork(100)
BuyHealth = SubHealth(100)
BuyStamina = SubStamina(100)
money = 100

def MarketScene():
    decisions = ["Steak", "Pork", "Health Potion", "Stamina Potion"]
    print(f"You have just arrived in Kingsforth's Marketplace! You have {money} Forthmite. What would you like?")
    userInput = ""
    while userInput not in decisions:
        print("Options: Steak/Pork/Health Potion/Stamina Potion")
        userInput = input()
        if userInput == "Steak":
            print(f"You purchased a Steak! You have {BuySteak} Forthmite left.")
        elif userInput == "Pork":
            print(f"You purchased Pork! You have {BuyPork} Forthmite left.")
        elif userInput == "Health Potion":
            print(f"You purchased a Health Potion! You have {BuyHealth} Forthmite left.")
        elif userInput == "Stamina Potion":
            print(f"You purchased a Stamina Potion! You have {BuyStamina} Forthmite left.")
        else:
            print("That is not an option.")

MarketScene()