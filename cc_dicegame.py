import random


def dice_game():
    high_score = 0
    while True:
        print("1) Roll Dice", "\n" "2) Leave Game")
        choice = input("Enter your choice: ")

        if choice == "1":
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print("You have rolled a...", dice1,
                  "\n" "You have rolled a...", dice2)
            newtotal = dice1 + dice2
            print("You have rolled a total of:", newtotal)
            if newtotal > high_score:
                high_score = newtotal
                print("New high score!")
            elif newtotal <= high_score:
                continue
        elif choice == "2":
            print("Goodbye")
            break


dice_game()
