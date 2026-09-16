# Make a character class with 3 subclasses - Warrior, Elfin, Wizord. Warrior: Health, axe, Higher Strength. Elf: Health, speed. Wizard: Health, Magic. 
# Two characters fight, attacks generate (random) damage on health, when health reaches 0, winner is declared.
# Print status of characters, attack value (damage)
import random
class Character():
    def __init__(self, name, weapon, damage, health = 100, dodge = random.randint(0, 1)):
        self.name = name
        self.health = health
        self.damage = damage
        self.dodge = dodge
        self.weapon = weapon

    def attack():
        opp.health -= random.randint(1,10)

class Wizard(Character):
    def __init__(self, "Shaft", pos_expression = "YEHAW", neg_expression = "YEOW"):
        super().__init__("Wizard", "Shaft", random.randint(20, 40), health, dodge)
        self.pos_expression = pos_expression
        self.neg_expression = neg_expression

class Elf(Character):
    def __init__(self, pos_expression = "YEHAW", neg_expression = "YEOW"):
        super().__init__("Elf", "Glock", random.randint(5,15), health, dodge)
        self.pos_expression = pos_expression
        self.neg_expression = neg_expression

class Warrior(Character):
    def __init__(self, pos_expression = "YEHAW", neg_expression = "YEOW"):
        super().__init__("Warrior", "Cutlass", random.randint(30, 55), health, dodge)
        self.pos_expression = pos_expression
        self.neg_expression = neg_expression

Brawler1 = input("Choose your first player")
Brawler2 = input("Choose your second player")
characters= [
    "Wizard": Wizard()
    "Elf" : Elf()
    "Warrior" : Warrior()
]
charcter[Brawler1]()
        

        