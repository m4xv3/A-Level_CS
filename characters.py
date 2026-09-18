import random
import time


class Character:
    def __init__(self, name, weapon, damage, health=100, dodge_chance=3,
                 pos_expression="YEHAW", neg_expression="YEOW"):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = weapon
        self.dodge_chance = dodge_chance
        self.pos_expression = pos_expression
        self.neg_expression = neg_expression

    def isdead(self):
        return self.health <= 0

    def attack(self, opponent):
        if random.randint(1, 10) <= opponent.dodge_chance:
            print(f"{opponent.name} dodged the attack!")
            time.sleep(0.5)
            print(f"{opponent.name}: '{opponent.pos_expression}'")
            time.sleep(1.5)
            print(f"{self.name} health: {self.health}hp")
            print(f"{opponent.name} health: {opponent.health}hp")
            time.sleep(2.5)
            return

        opponent.health -= self.damage
        if opponent.health < 0:
            opponent.health = 0

        print(f"{self.name} hit {opponent.name}: {self.damage}dmg")
        time.sleep(0.5)
        print(f"{opponent.name}: '{opponent.neg_expression}'")
        time.sleep(1.5)
        print(f"{self.name} health: {self.health}hp")
        print(f"{opponent.name} health: {opponent.health}hp")
        time.sleep(2.5)

    def brawl1(self, opponent):
        self.attack(opponent)

    def brawl2(self, opponent):
        self.attack(opponent)

    @staticmethod
    def selection():
        characters_dict = {
            "wizard": Wizard(),
            "elf": Elf(),
            "warrior": Warrior(),
        }

        while True:
            choice1 = input("Choose your first player (Warrior, Elf, Wizard): \n").strip().lower()
            if choice1 in characters_dict:
                break
            print("Invalid Selection. Please try again.")

        while True:
            choice2 = input("Choose your second player (Warrior, Elf, Wizard): \n").strip().lower()
            if choice2 in characters_dict:
                break
            print("Invalid Selection. Please try again.")

        return characters_dict[choice1], characters_dict[choice2]


class Wizard(Character):
    def __init__(self, pos_expression="YEHAW", neg_expression="YEOW"):
        super().__init__("Wizard", "Staff", random.randint(20, 40),
                         dodge_chance=3, pos_expression=pos_expression,
                         neg_expression=neg_expression)


class Elf(Character):
    def __init__(self, pos_expression="YEHAW", neg_expression="YEOW"):
        super().__init__("Elf", "Bow", random.randint(5, 15),
                         dodge_chance=4, pos_expression=pos_expression,
                         neg_expression=neg_expression)


class Warrior(Character):
    def __init__(self, pos_expression="YEHAW", neg_expression="YEOW"):
        super().__init__("Warrior", "Sword", random.randint(30, 55),
                         dodge_chance=2, pos_expression=pos_expression,
                         neg_expression=neg_expression)


if __name__ == "__main__":
    brawler1, brawler2 = Character.selection()

