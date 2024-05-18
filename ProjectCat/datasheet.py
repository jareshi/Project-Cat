# This will contain the classes that will be used in the game

class Weapon:
    def __init__(w, name: str, type: str, damage: int, range: int = None, bonus: int = None) -> None:
        w.name = name
        w.type = type
        w.damage = damage
        w.range = range
        w.bonus = bonus

class Character:
    def __init__(c, name: str, characterClass: str, health: int, attack: int, magic: int, defense: int, resistance: int, speed: int, mana: int, weapon: Weapon = None) -> None:
        c.name = name
        c.characterClass = characterClass
        c.health = health
        c.healthMax = health
        c.attack = attack
        c.defense = defense
        c.magic = magic
        c.resistance = resistance
        c.speed = speed
        c.mana = mana
        c.manaMax = mana
        c.weapon = weapon