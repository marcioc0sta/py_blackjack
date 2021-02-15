from random import shuffle


def create_deck():
    deck = []
    faceValues = ['A', 'J', 'Q', 'K']

    for i in range(4):
        for card in range(2, 11):
            deck.append(str(card))
        for card in faceValues:
            deck.append(card)

    shuffle(deck)
    return deck


class Player:
    def __init__(self, hand=[], money=100):
        self.hand = hand
        self.score = self.set_score()
        self.money = money
        self.bet = 0

    def __str__(self):
        current_hand = ""
        for card in self.hand:
            current_hand += str(card) + " "

        return f"{current_hand} score: {str(self.score)}"

    def set_score(self):
        self.score = 0
        ace_counter = 0

        face_cards_dict = {"A": 11, "J": 10, "Q": 10, "K": 10, "2": 2, "3": 3,
                           "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}

        for card in self.hand:
            self.score += face_cards_dict[card]
            if card == "A":
                ace_counter += 1
            if self.score > 21 and ace_counter != 0:
                self.score -= 10
                ace_counter -= 1

        return self.score

    def hit(self, card):
        self.hand.append(card)
        self.score = self.set_score()

    def play(self, new_hand):
        self.hand = new_hand
        self.score = self.set_score()

    def bet_money(self, amount):
        self.money -= amount
        self.bet += amount

    def win(self, result):
        black_jack = self.score == 21 and len(self.hand) == 2
        if result:
            if black_jack:
                self.money += 2.5*self.bet
            else:
                self.money += 2*self.bet
            self.bet = 0
        else:
            self.bet = 0


def print_house(House):
    for card in range(len(House.hand)):
        if card == 0:
            print('House: *', end=" ")
        elif card == len(House.hand) - 1:
            print(f'House: {House.hand[card]}')
        else:
            print(f'House: {House.hand[card]}', end=" ")


card_deck = create_deck()
first_hand = [card_deck.pop(), card_deck.pop()]
second_hand = [card_deck.pop(), card_deck.pop()]

player_1 = Player(first_hand)
house = Player(second_hand)

print_house(house)
print(player_1)

while(player_1.score < 21):
    action = input("Do you want another card? (y/n): ")

    if action == 'y':
        player_1.hit(card_deck.pop())
        print(player_1)
        print_house(house)
    else:
        break

print(house)
