import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    """
    creates an object 'Card' that has suit, rank and value
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    """
    creates a deck of 52 unique card objects
    """
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        """
        shuffles the deck we just created
        """
        random.shuffle(self.all_cards)

    def deal_one(self):
        """
        removes last card of the deck and returns it
        :return: a card object
        """
        return self.all_cards.pop()


class Player:
    """
    creates a player class object that can remove a card from hand and take in the cards it won
    """
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        """
        takes the last card from a player's hand and returns it
        :return: a card object
        """
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        """
        add cards into the players hand
        :param new_cards: the cards in play
        """
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


game_on = True
player_one = Player('One')
player_two = Player('Two')
new_deck = Deck()
new_deck.shuffle()
print(new_deck.all_cards)
for card in range(26):  # splitting the new created deck into 2
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
round_number = 0  # counter for rounds that passed

while game_on:
    round_number += 1
    print(f'Round {round_number}')
    if len(player_one.all_cards) == 0:  # checking if P1 has enough cards to play
        print(f'{player_one} lost')
        game_on = False
        break
    if len(player_two.all_cards) == 0:  # checking if P2 has enough cards to play
        print(f'{player_two} lost!')
        game_on = False
        break
    player_one_cards = [player_one.remove_one()]  # creates a list with the card in play from P1
    player_two_cards = [player_two.remove_one()]  # creates a list with the card in play from P2

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:  # checking who has the bigger last played card value
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print('War')
            if len(player_one.all_cards) < player_one_cards[-1].value:  # checking to see if the player has enough cards
                                                                        # to play war
                print("Player One doesn't have enough cards to play!")
                print("player Two wins!")
                game_on = False
                break

            elif len(player_two.all_cards) < player_two_cards[-1].value:
                print("Player Two doesn't have enough cards to play!")
                print("player One wins!")
                game_on = False
                break
            else:
                for num in range(1, player_one_cards[-1].value):  # each player has to play cards value number of cards
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
