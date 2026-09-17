# Make a character class with 3 subclasses - Warrior, Elf, Wizard.
# Warrior: Health, axe, Higher Strength. Elf: Health, speed. Wizard: Health, Magic.
# Two characters fight, attacks generate (random) damage on health, when health reaches 0, winner is declared.
# Print status of characters, attack value (damage)
import random
import time

from characters import Wizard, Elf, Warrior


def main():
    choice1 = input("Choose your first player: \n").strip().lower()
    choice2 = input("Choose your second player: \n").strip().lower()

    characters = {
        "wizard": Wizard,
        "elf": Elf,
        "warrior": Warrior,
    }

    if choice1 not in characters or choice2 not in characters:
        print("Invalid choice. Please choose wizard, elf, or warrior.")
        return

    brawler1 = characters[choice1]()
    brawler2 = characters[choice2]()
    num_rounds = int(input("How many rounds? \n"))

    for round_number in range(1, num_rounds + 1):
        print("\n" + "-" * 30)
        print(f"Round {round_number}")
        print("-" * 30)
        time.sleep(1.5)

        attacker, defender = random.sample([brawler1, brawler2], k=2)
        attacker.attack(defender)
        print(f"{brawler1.name}: {brawler1.health} HP")
        print(f"{brawler2.name}: {brawler2.health} HP")
        time.sleep(2.0)

        if brawler1.is_dead() or brawler2.is_dead():
            break

    if brawler1.is_dead():
        winner = brawler2.name
        loser = brawler1.name
    elif brawler2.is_dead():
        winner = brawler1.name
        loser = brawler2.name
    else:
        winner = "Nobody"
        loser = "Nobody"

    print(f"Finished: {winner} has defeated {loser}!")


if __name__ == "__main__":
    main()