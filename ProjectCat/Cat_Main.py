# This will be the main file that will be used to run the game.

from random import randint
from Cat_AI import LLM_generation # Importing the LLM generation function
from datasheet import Character # Importing the character class
import armory

intro_ASCII = r"""
 ._       __          ____
;  `\--,-' /`)    _.-'    `-._
 \_/    ' | /`--,'            `-.     .--....____
  /                              `._.'           `---...
  |-.   _      ;                        .-----..._______)
,,\q/ (q_>'_...                      .-'
===/ ; _.-'~~-             /       ,'
`""`-'_,;  `""         ___(       |
         \         ; /'/   \      \
          `.      //' (    ;`\    `\
          / \    ;     `-  /  `-.  /
         (  (;   ;     (__/    /  /
          \,_)\  ;           ,'  /
  .-.          |  |           `--'
 ("_.)-._     (__,>
"""
print(intro_ASCII)

# Initializing the character
print("Welcome to the region of Wolfspine. What is your name?")

adventurerName = str(input())
print("What is your class (please enter 1-6)?")
print("1. Warrior\n2. Mage\n3. Rogue\n4. Paladin\n5. Cleric\n6. Ranger")

# Setting randomized stats based on class
while(True):
    adventurerClass = int(input())
    if (1 <= adventurerClass <= 6):
        if (adventurerClass == 1):
            adventurerClass = "Warrior"
            adventurerHealth = randint(80, 100)
            adventurerAttack = randint(70, 80)
            adventurerMagic = randint(0, 10)
            adventurerDefense = randint(70, 80)
            adventurerResistance = randint(40, 50)
            adventurerSpeed = randint(40, 50)
            adventurerMana = randint(0, 10)
            adventurerWeapon = armory.ironSword
        elif (adventurerClass == 2):
            adventurerClass = "Mage"
            adventurerHealth = randint(30, 40)
            adventurerAttack = randint(10, 20)
            adventurerMagic = randint(80, 90)
            adventurerDefense = randint(10, 20)
            adventurerResistance = randint(60, 70)
            adventurerSpeed = randint(30, 40)
            adventurerMana = randint(80, 90)
            adventurerWeapon = armory.apprenticeStaff
        elif (adventurerClass == 3):
            adventurerClass = "Rogue"
            adventurerHealth = randint(60, 70)
            adventurerAttack = randint(60, 70)
            adventurerMagic = randint(10, 20)
            adventurerDefense = randint(40, 50)
            adventurerResistance = randint(30, 40)
            adventurerSpeed = randint(80, 90)
            adventurerMana = randint(20, 30)
            adventurerWeapon = armory.ironDaggers
        elif (adventurerClass == 4):
            adventurerClass = "Paladin"
            adventurerHealth = randint(80, 90)
            adventurerAttack = randint(60, 70)
            adventurerMagic = randint(40, 50)
            adventurerDefense = randint(60, 70)
            adventurerResistance = randint(70, 80)
            adventurerSpeed = randint(30, 40)
            adventurerMana = randint(40, 50)
            adventurerWeapon = armory.ironLongsword
        elif (adventurerClass == 5):
            adventurerClass = "Cleric"
            adventurerHealth = randint(70, 80)
            adventurerAttack = randint(40, 50)
            adventurerMagic = randint(60, 70)
            adventurerDefense = randint(50, 60)
            adventurerSpeed = randint(30, 40)
            adventurerResistance = randint(70, 80)
            adventurerMana = randint(60, 70)
            adventurerWeapon = armory.woodenMace
        elif (adventurerClass == 6):
            adventurerClass = "Ranger"
            adventurerHealth = randint(70, 80)
            adventurerAttack = randint(60, 70)
            adventurerMagic = randint(20, 30)
            adventurerDefense = randint(40, 50)
            adventurerSpeed = randint(70, 80)
            adventurerResistance = randint(50, 60)
            adventurerMana = randint(20, 30)
            adventurerWeapon = armory.shortBow
        break

    else:
        print("Invalid Input\nPlease try again:")

adventurer = Character(adventurerName, adventurerClass, adventurerHealth, adventurerAttack, adventurerMagic, adventurerDefense, adventurerResistance, adventurerSpeed, adventurerMana, adventurerWeapon)

print(f"\n\nStats Sheet:\n\
Name: {adventurer.name}\n\
Class: {adventurer.characterClass}\n\
Health: {adventurer.health}\n\
Attack: {adventurer.attack}\n\
Magic: {adventurer.magic}\n\
Defense: {adventurer.defense}\n\
Resistance: {adventurer.resistance}\n\
Speed: {adventurer.speed}\n\
Mana: {adventurer.mana}\n\
Weapon: {adventurer.weapon.name}\n\
")

print("\n\nLet's start the adventure!")

adventurerHistory = []
adventurerQuery = f"{adventurer.name} has just left their home to embark on a journey."
path = LLM_generation(adventurerHistory, adventurerQuery)
path = path.strip()
adventurerHistory.append(path)
print(path)

while(True):
    