# Make a character class with 3 subclasses - Warrior, Elfin, Wizord. Warrior: Health, axe, Higher Strength. Elf: Health, speed. Wizard: Health, Magic. 
# Two characters fight, attacks generate (random) damage on health, when health reaches 0, winner is declared.
# Print status of characters, attack value (damage)
import random
import time
from characters import Character, Wizard, Elf, Warrior

Choice1 = input("Choose your first player: \n").strip().lower()
Choice2 = input("Choose your second player: \n").strip().lower()
characters= {
    "wizard": Wizard(),
    "elf" : Elf(),
    "warrior" : Warrior()
}
Brawler1 = characters[Choice1]       
Brawler2 = characters[Choice2]
num_rounds = int(input("How Many Rounds? \n"))
while not Brawler1.isdead() and not Brawler2.isdead():
    for i in range(num_rounds):
        print(f"Round {i}")
        time.sleep(0.5)
        num = random.randint(1,2)
        if num == 1:
            Brawler1.brawl1()
        elif num == 2:
            Brawler2.brawl2()
            time.sleep(0.5)
    if Brawler1.health == 0:
        winner = Brawler2.name
        loser = Brawler1.name
    elif Brawler2.health == 0:
        winner = Brawler1.name
        loser = Brawler2.name
print(f"Finished: {winner} has defeated {loser}!")