import random
from main import Brawler1, Brawler2
class Character():
    def __init__(self, name, weapon, damage, health = 100, dodge = random.randint(0, 1), pos_expression = "YEHAW", neg_expression = "YEOW"):
        self.name = name
        self.health = health
        self.damage = damage
        self.dodge = dodge
        self.weapon = weapon
        self.pos_expression = pos_expression
        self.neg_expression = neg_expression

    def brawl1():
        if isinstance(Brawler1, Wizard):
            if random.randint(0,1) == 1:
                Brawler2.health -= Brawler1.damage
                print(Brawler2.neg_expression)
                print(f"{Brawler2.name} health: {Brawler2.health}")
            else:
                print(f"{Brawler2} dodged the attack!")
                print(Brawler2.pos_expression)

        elif isinstance(Brawler1, Elf):
            if random.randint(0,1) == 1:
                Brawler2.health -= Brawler1.damage
                print(Brawler2.neg_expression)
                print(f"{Brawler2.name} health: {Brawler2.health}")
            else:
                print(f"{Brawler2.name} dodged the attack!")
                print(Brawler2.pos_expression)               
        elif isinstance(Brawler1, Warrior):
            if random.randint(0,1) == 1:
                Brawler2.health -= Brawler1.damage
                print(Brawler2.neg_expression)
                print(f"{Brawler2.name} health: {Brawler2.health}")
            else:
                print(f"{Brawler2.name} dodged the attack!")
                print(Brawler2.pos_expression)

    def brawl2():
        if isinstance(Brawler2, Wizard):
            if random.randint(0,1) == 1:
                Brawler1.health -= Brawler2.damage
                print(Brawler1.neg_expression)
                print(f"{Brawler1.name} health: {Brawler1.health}")
            else:
                print(f"{Brawler1.name} dodged the attack!")
                print(Brawler1.pos_expression)
        elif isinstance(Brawler2, Elf):
            if random.randint(0,1) == 1:
                Brawler1.health -= Brawler2.damage 
                print(Brawler1.neg_expression)
                print(f"{Brawler1.name} health: {Brawler1.health}")
            else:
                print(f"{Brawler1.name} dodged the attack!")
                print(Brawler1.pos_expression)
        elif isinstance(Brawler2, Warrior):
            if random.randint(0,1) == 1:
                Brawler1.health -= Brawler2.damage
                print(f"{Brawler1.name} dodged the attack!")
                print(Brawler1.pos_expression)

    def isdead(self):
        if self.health == 0:
            return True

class Wizard(Character):
    def __init__(self, pos_expression = "YEHAW", neg_expression = "YEOW"):
        super().__init__("Wizard", "Shaft", random.randint(20, 40))
        self.pos_expression = pos_expression
        self.neg_expression = neg_expression

class Elf(Character):
    def __init__(self, pos_expression = "YEHAW", neg_expression = "YEOW"):
        super().__init__("Elf", "Glock", random.randint(5,15))
        self.pos_expression = pos_expression
        self.neg_expression = neg_expression

class Warrior(Character):
    def __init__(self, pos_expression = "YEHAW", neg_expression = "YEOW"):
        super().__init__("Warrior", "Cutlass", random.randint(30, 55))
        self.pos_expression = pos_expression
        self.neg_expression = neg_expression
