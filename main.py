from random import shuffle

def createDeck():
    deck = []
    faceValues = ['A', 'J', 'Q', 'K']

    for i in range(4):
        for card in range(2, 11):
            deck.append(str(card))
        for card in faceValues:
            deck.append(card)

    shuffle(deck)
    return deck


cardDeck = createDeck()
print(cardDeck)
