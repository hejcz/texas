class Game:
    def __init__(self, send_to_all, send_to_single) -> None:
        super().__init__()
        # send to all wysyła informację do wszystkich, np. o tym że gra się rozpoczęła
        # przykład: self.send_to_all("Player {} bid for {}".format(player_id, amount))
        self.send_to_all = send_to_all
        # send to single wysyła informację do gracza o określonym id
        # przykład: self.send_to_single(player_id, "Player {} bid for {}".format(player_id, amount))
        self.send_to_single = send_to_single

    def raise_money(self, player_id, amount):
        self.send_to_all("Player {} raised by {}".format(player_id, amount))

    def check(self, player_id):
        self.send_to_all(player_id, "checks")
        pass

    def start_game(self):
        self.send_to_all("Let's start the game")
        pass

    def fold(self, player_id):
        self.send_to_all(player_id, "has folded")
        pass

    def call(self, player_id, amount):
        self.send_to_single(player_id, "you spent {}".format(amount))
        pass

    def check_cards(self, player_id):
        pass


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
        for s in suits:
            for n in numbers:
                cards.append(Card(suit, number))

        self._cards = cards