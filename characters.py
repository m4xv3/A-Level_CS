import random


class BrawlerChar:
    def __init__(self, name, weapon, min_damage, max_damage, health=100):
        self.name = name
        self.weapon = weapon
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.health = health

    def attack(self, opponent):
        damage = random.randint(self.min_damage, self.max_damage)
        opponent.health = max(0, opponent.health - damage)
        print(f"{self.name} attacks with {self.weapon} for {damage} damage.")
        print(f"{opponent.name} health: {opponent.health}")
        return damage

    def is_dead(self):
        return self.health <= 0


class Wizard(BrawlerChar):
    def __init__(self, name="Wizard"):
        super().__init__(name, "magic staff", 15, 35, 90)


class Elf(BrawlerChar):
    def __init__(self, name="Elf"):
        super().__init__(name, "bow", 10, 25, 80)


class Warrior(BrawlerChar):
    def __init__(self, name="Warrior"):
        super().__init__(name, "axe", 20, 45, 120)
