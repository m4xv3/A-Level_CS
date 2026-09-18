from characters import *
import random
import time
while brawler1.health > 0 and brawler2.health > 0:
    random_num = random.randint(0,1)
    if random_num == 0:
        brawler1.brawl1()
    elif random_num == 1:
        brawler2.brawl2()

if brawler1.health <= 0:
    winner = brawler2.name
    loser = brawler1.name
elif brawler2.health <= 0:
    winner = brawler1.name
    loser = brawler2.name
time.sleep(1)
print(f"{winner} has defeated {loser}!")