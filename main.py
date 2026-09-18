from characters import *
import random
import time

start = input("Welcome, would you like to begin? (Y/N) \n").strip().lower()
start_chars = ["start", "yes", "y", "yh", "yeah", "ye", "ya"]
stop_chars = ["stop", "no", "n", "nah"]

while start not in start_chars:
    if start in stop_chars:
        raise SystemExit("Game Closed")
        break
    print("Invalid input. Please try again.")
    start = input("Welcome, would you like to begin? (Y/N) \n").strip().lower()

if start in start_chars:
    brawler1, brawler2 = Character.selection()


round_number = 0
while not brawler1.isdead() and not brawler2.isdead():
    round_number += 1
    print("-" * 30)
    print(f"Round: {round_number}")
    print("-" * 30)
    time.sleep(2.5)

    attacker = random.choice([brawler1, brawler2])
    defender = brawler2 if attacker == brawler1 else brawler1
    attacker.attack(defender)

if brawler1.health <= 0:
    winner = brawler2.name
    loser = brawler1.name
elif brawler2.health <= 0:
    winner = brawler1.name
    loser = brawler2.name

print(f"{winner} has defeated {loser}!")