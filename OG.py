import random
class Character():
    def __init__(self, name, weapon, damage, health = 100, dodge = random.randint(0, 1), pos_expression = "YEHAW", neg_expression = "YEOW"):
        self.name = name
        self.health = health
        self.damage = damage
        self.dodge = dodge
        self.weapon = weapon
        self.pos_expression = pos_expression
        self.neg_expression = neg_expression

    def brawl1(self):
        if isinstance(brawler1, Wizard):
            if random.randint(0,1) == 1:
                brawler2.health -= brawler1.damage
                print(f"{brawler2}: {brawler2.neg_expression}")
                print(f"{brawler2.name} health: {brawler2.health}")
            else:
                print(f"{brawler2} dodged the attack!")
                print(f"{brawler2}: {brawler2.pos_expression}")

        elif isinstance(brawler1, Elf):
            if random.randint(0,1) == 1:
                brawler2.health -= brawler1.damage
                print(f"{brawler2}: {brawler2.neg_expression}")
                print(f"{brawler2.name} health: {brawler2.health}")
            else:
                print(f"{brawler2.name} dodged the attack!")
                print(f"{brawler2}: {brawler2.pos_expression}")               
        elif isinstance(brawler1, Warrior):
            if random.randint(0,1) == 1:
                brawler2.health -= brawler1.damage
                print(f"{brawler2}: {brawler2.neg_expression}")
                print(f"{brawler2.name} health: {brawler2.health}")
            else:
                print(f"{brawler2.name} dodged the attack!")
                print(f"{brawler2}: {brawler2.neg_expression}")

    def brawl2(self):
        if isinstance(brawler2, Wizard):
            if random.randint(0,1) == 1:
                brawler1.health -= brawler2.damage
                print(brawler1.neg_expression)
                print(f"{brawler1.name} health: {brawler1.health}")
            else:
                print(f"{brawler1.name} dodged the attack!")
                print(brawler1.pos_expression)
        elif isinstance(brawler2, Elf):
            if random.randint(0,1) == 1:
                brawler1.health -= brawler2.damage 
                print(brawler1.neg_expression)
                print(f"{brawler1.name} health: {brawler1.health}")
            else:
                print(f"{brawler1.name} dodged the attack!")
                print(brawler1.pos_expression)
        elif isinstance(brawler2, Warrior):
            if random.randint(0,1) == 1:
                brawler1.health -= brawler2.damage
                print(f"{brawler1.name} dodged the attack!")
                print(brawler1.pos_expression)




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

def selection():
    characters_dict = {
        "Wizard": Wizard(),
        "Elf" : Elf(),
        "Warrior" : Warrior()
        }
    selection_loop = True
    while selection_loop:
        choice1 = input("Choose your first player (Warrior, Elf, Wizard): \n")
        if choice1 in characters_dict:
            selection_loop = False
        else:
            print("Invalid Selection. Please try again.")
    selection_loop = True
    while selection_loop:
        choice2 = input("Choose your second player (Warrior, Elf, Wizard): \n")
        if choice2 in characters_dict:
            selection_loop = False
        else:
            print("Invalid Selection. Please try again.")
    return characters_dict[choice1], characters_dict[choice2]


brawler1, brawler2 = selection()
print("Round 1")
