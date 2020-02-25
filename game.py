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
        self.send_to_single(player_id, "ok")

    def check(self, player_id):
        self.send_to_all(player_id, "checks")
        pass

    def skip(self, player_id):
        pass

    def start_game(self, player_id):
        self.send_to_all("Let's start the game")
        pass

    def fold(self, player_id):
        self.send_to_all(player_id, "has folded")
        pass

    def call(self, player_id, amount):
        self.send_to_all(player_id, "you spent {}".format(amount))
        pass

    def check_cards(self, player_id):
        pass
