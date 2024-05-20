# This will contain all the monsters that the user will encounter in the game

from datasheet import Character
from random import randint

# Beginner monsters
goblin  =  Character(
    name = "Goblin",
    characterClass = "Monster",
    health = randint(30, 40),
    attack = randint(10, 15),
    magic = randint(0, 5),
    defense = randint(10, 15),
    resistance = randint(5, 10),
    speed = randint(20, 25),
    mana = 0
)

fireDrake  =  Character(
    name = "Fire Drake",
    characterClass = "Monster",
    health = randint(50, 60),
    attack = randint(15, 20),
    magic = randint(20, 25),
    defense = randint(15, 20),
    resistance = randint(20, 25),
    speed = randint(10, 15),
    mana = randint(30, 40)
)

ogre  =  Character(
    name = "Ogre",
    characterClass = "Monster",
    health = randint(70, 80),
    attack = randint(20, 25),
    magic = 0,
    defense = randint(20, 25),
    resistance = randint(10, 15),
    speed = randint(5, 10),
    mana = 0
)

giantSpider  =  Character(
    name = "Giant Spider",
    characterClass = "Monster",
    health = randint(40, 50),
    attack = randint(15, 20),
    magic = randint(0, 5),
    defense = randint(10, 15),
    resistance = randint(10, 15),
    speed = randint(25, 30),
    mana = 0
)

shadowMage  =  Character(
    name = "Shadow Mage",
    characterClass = "Monster",
    health = randint(30, 40),
    attack = randint(5, 10),
    magic = randint(25, 30),
    defense = randint(5, 10),
    resistance = randint(20, 25),
    speed = randint(15, 20),
    mana = randint(30, 40)
)

elementalDragon = Character(
    name = "Marvin, the Elemental Dragon",
    characterClass = "Final Monster",
    health = randint(200, 250),
    attack = randint(50, 60),
    magic = randint(60, 70),
    defense = randint(50, 60),
    resistance = randint(55, 65),
    speed = randint(40, 50),
    mana = randint(70, 80)
)