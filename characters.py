import random
import time

class Character():
    def __init__(self, name, weapon, damage, health = 100, dodge = random.randint(0, 1), pos_expression = "YEHAW", neg_expression = "YEOW"):
        self.name = name
        self.health = health
        self.damage = damage
        self.dodge = dodge
        self.weapon = weapon
        self.pos_expression = pos_expression
        self.neg_expression = neg_expression

    def isdead(self):
        if self.health <= 0:
            return True

    def brawl1(self):
        count = 0
        while not brawler1.isdead() and not brawler2.isdead():
            count += 1
            time.sleep(1)
            print("\n")
            print("-" * 30)
            print("\n")
            print(f"Round: {count}")
            print("\n")
            print("-" * 30)
            time.sleep(1)
            if isinstance(brawler1.name, Wizard):
                if random.randint(0,1) == 1:
                    brawler2.health -= brawler1.damage
                    print(f"{brawler2.name}: {brawler2.neg_expression}")
                    time.sleep(1)
                    print(f"{brawler2.name} health: {brawler2.health}")
                    time.sleep(1)
                else:
                    print(f"{brawler2.name} dodged the attack!")
                    time.sleep(1)
                    print(f"{brawler2.name}: {brawler2.pos_expression}")
                    time.sleep(1)

            elif isinstance(brawler1, Elf):
                if random.randint(0,1) == 1:
                    brawler2.health -= brawler1.damage
                    print(f"{brawler2.name}: {brawler2.neg_expression}")
                    time.sleep(1)
                    print(f"{brawler2.name} health: {brawler2.health}")
                    time.sleep(1)
                else:
                    print(f"{brawler2.name} dodged the attack!")
                    time.sleep(1)
                    print(f"{brawler2.name}: {brawler2.pos_expression}")  
                    time.sleep(1)             
            elif isinstance(brawler1, Warrior):
                if random.randint(0,1) == 1:
                    brawler2.health -= brawler1.damage
                    print(f"{brawler2.name}: {brawler2.neg_expression}")
                    time.sleep(1)
                    print(f"{brawler2.name} health: {brawler2.health}")
                    time.sleep(1)
                else:
                    print(f"{brawler2.name} dodged the attack!")
                    time.sleep(1)
                    print(f"{brawler2.name}: {brawler2.neg_expression}")
                    time.sleep(1)

    def brawl2(self):
        count = 0
        while brawler1.health > 0 and brawler2.health > 0:
            count += 1
            time.sleep(1)
            print("\n")
            print("-" * 30)
            print("\n")
            print(f"Round: {count}")
            print("\n")
            print("-" * 30)
            time.sleep(1)
            if isinstance(brawler2.name, Wizard):
                if random.randint(0,1) == 1:
                    brawler1.health -= brawler2.damage
                    print(f"{brawler1.name}: {brawler1.neg_expression}")
                    time.sleep(1)
                    print(f"{brawler1.name} health: {brawler1.health}")
                    time.sleep(1)
                    print(f"{brawler2.name} health: {brawler2.health}")
                    time.sleep(1)
                else:
                    print(f"{brawler1.name} dodged the attack!")
                    time.sleep(1)
                    print(brawler1.pos_expression)
                    time.sleep(1)
            elif isinstance(brawler2.name, Elf):
                if random.randint(0,1) == 1:
                    brawler1.health -= brawler2.damage 
                    print(brawler1.neg_expression)
                    time.sleep(1)
                    print(f"{brawler1.name} health: {brawler1.health}")
                    time.sleep(1)
                else:
                    print(f"{brawler1.name} dodged the attack!")
                    time.sleep(1)
                    print(brawler1.pos_expression)
                    time.sleep(1)
            elif isinstance(brawler2.name, Warrior):
                if random.randint(0,1) == 1:
                    brawler1.health -= brawler2.damage
                    print(f"{brawler1.name} dodged the attack!")
                    time.sleep(1)
                    print(brawler1.pos_expression)
                    time.sleep(1)

    def selection():
        characters_dict = {
            "wizard": Wizard(),
            "elf" : Elf(),
            "warrior" : Warrior()
            }
        selection_loop = True
        while selection_loop:
            choice1 = input("Choose your first player (Warrior, Elf, Wizard): \n").strip().lower()
            if choice1 in characters_dict:
                selection_loop = False
            else:
                print("Invalid Selection. Please try again.")
        selection_loop = True
        while selection_loop:
            choice2 = input("Choose your second player (Warrior, Elf, Wizard): \n").strip().lower()
            if choice2 in characters_dict:
                selection_loop = False
            else:
                print("Invalid Selection. Please try again.")
        return characters_dict[choice1], characters_dict[choice2]





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

brawler1, brawler2 = Character.selection()

