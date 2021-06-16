# While Loop

card_deck = [2,5,1,5,3,4,7]
hand = []

while sum(hand) <= 17:
    hand.append(card_deck.pop())

print(hand)
