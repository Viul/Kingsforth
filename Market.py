markets = ['Steak', 'Porkchop', 'Health Potion', 'Stamina Potion']
Money = 100
Steak = 7
Porkchop = 5
HealthPotion = 20
StaminaPotion = 20
print(f"Welcome to the Kingsforth Market! You have {Money} Forthmite. This is what we have for sale:")

for item in markets:
    print(item)

print("What would you like?")
while True:
    decision = input()
    if decision == "Steak":
        print(f"A Steak? Alright that will be {Steak} Forthmite.")
        balance = int(Money - Steak)
        print(f"You bought a {markets[0]}! You have {balance} Forthmite left.")
        break
    elif decision == "Porkchop":
        print(f"A Porkchop? Alright that will be {Porkchop} Forthmite.")
        balance = int(Money - Porkchop)
        print(f"You bought a {markets[1]}! You have {balance} Forthmite left.")
        break
    elif decision == "HealthPotion":
        print(f"A Health Potion? Alright that will be {HealthPotion} Forthmite.")
        balance = int(Money - HealthPotion)
        print(f"You bought a {markets[2]}! You have {balance} Forthmite left.")
        break
    elif decision == ("Stamina Potion"):
        print(f"A Stamina Potion? Alright that will be {StaminaPotion} Forthmite.")
        balance = int(Money - HealthPotion)
        print(f"You bought a {markets[3]}! You have {balance} Forthmite left.")
        break
    else:
        print("That is not an option.")