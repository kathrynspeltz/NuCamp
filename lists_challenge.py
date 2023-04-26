import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    card = input("Choose a card or enter Q and enter to quit")
    if card == "Q":
        break
    elif card == "":
        card_position = str(random.choice(diamonds))
        hand.append(card_position)
        diamonds.remove(card_position)
        print(f"Current remaining cards:{diamonds}")
        print(f"Cards you have in your hand:{hand}")

if not diamonds:
    print("There are no more cards to pick")
