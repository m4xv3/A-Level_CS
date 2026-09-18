from characters import Character, Wizard, Elf, Warrior, brawler1, brawler2
import random
import time
while brawler1.health > 0 and brawler2.health > 0:
    random_num = random.randint(0,1)
    if random_num == 0:
        Character.brawl1()

    elif random_num == 1:
        attacker = brawler2
        defender = brawler1
        Character.brawl2()
if brawler1.health == 0:
    winner = brawler2
    loser = brawler1
elif brawler2.health == 0:
    winner = brawler1
    loser = brawler2
print(f"{winner} has defeated {loser}!")