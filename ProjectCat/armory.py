# This will contain all the possible weapons (although there will only be 12 for simplicity)

from datasheet import Weapon

# Warrior Weapons
ironSword = Weapon(
    name = "Iron Sword",
    type = "sharp",
    damage = 12
)

dragonboneSword = Weapon(
    name = "Dragonbone Sword",
    type = "sharp",
    damage = 24,
    bonus = 12
)

# Mage Weapons
apprenticeStaff = Weapon(
    name = "Apprentice Staff",
    type = "magic",
    damage = 10,
    range = 20,
    bonus = 6
)

archmageStaff = Weapon(
    name = "Archmage Staff",
    type = "magic",
    damage = 20,
    range = 40,
    bonus = 10
)

# Rogue Weapons
ironDaggers = Weapon(
    name = "Iron Daggers",
    type = "sharp",
    damage = 6,
    bonus  = 2
)

shadowDaggers = Weapon(
    name = "Shadow Daggers",
    type = "sharp",
    damage = 16,
    bonus = 10
)

# Paladin Weapons
ironLongsword = Weapon(
    name = "Iron Longsword",
    type = "sharp",
    damage = 16
)

holyAvenger = Weapon(
    name = "Holy Avenger",
    type = "sharp",
    damage = 32,
    bonus = 10
)

# Cleric Weapons
woodenMace = Weapon(
    name = "Wooden Mace",
    type = "blunt",
    damage = 10
)

divineHammer = Weapon(
    name = "Divine Hammer",
    type = "blunt",
    damage = 18,
    bonus = 10
)

# Ranger Weapons
shortBow = Weapon(
    name = "Short Bow",
    type = "ranged",
    damage = 8,
    range = 50,
)

elvenLongbow = Weapon(
    name = "Elven Longbow",
    type = "ranged",
    damage = 20,
    range = 100,
    bonus = 10
)