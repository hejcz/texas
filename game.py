import random


class Game:
    def __init__(self, send_to_all, send_to_single) -> None:
        super().__init__()
        self.send_to_all = send_to_all
        self.send_to_single = send_to_single
        self.players_count = 0
        self.deck = Deck()
        self.players = []

    def raise_money(self, player_id, amount):
        self.send_to_all("Player {} raised by {}".format(player_id, amount))

    def check(self, player_id):
        self.send_to_all("{} checks".format(player_id))
        pass

    def start_game(self):
        self.send_to_all("Let's start the game")
        self.shuffle()
        for i in self.players:
            self.send_to_single(i, )
        pass

    def fold(self, player_id):
        self.send_to_all("{} has folded".format(player_id))
        pass

    def call(self, player_id, amount):
        self.send_to_single(player_id, "you spent {}".format(amount))
        pass

    def check_cards(self, player_id):
        pass

    def join_game(self, player_id):
        self.send_to_all("{} joined".format(player_id))
        self.players_count += 1
        self.players.append(player_id)

    def shuffle(self):
        random.shuffle(self.deck._cards)

    def deal_cards(self, x):
        for i in range(x):
            for i in range(players):
                cards2 = self.deck._cards.pop(0)
                self.send_to_single(i, cards2)


class Card:

    def __init__(self, suit, number):
        self._suit = suit
        self._number = number

    def __repr__(self):
        return self._number + " of " + self._suit

    def suit(self):
        return self._suit


class Deck:

    def __init__(self):
        self._cards = []
        self.populate()
        print(self._cards)

    def populate(self):
        suits = ["hearts", "diamonds", "clubs", "spades"]
        numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        cards = []
        for suit in suits:
            for number in numbers:
                cards.append(Card(suit, number))

        self._cards = cards



