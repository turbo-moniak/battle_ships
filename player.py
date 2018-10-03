class Player(object):
    def __init__(self, name):
        self.name = name
        self.fleet = []
        self.sunken_ships = {"battleship": 0, "cruiser": 0, "destroyer": 0, "submarine": 0}

    def update_sunken_ships(self, name):
        self.sunken_ships["name"] = self.sunken_ships["name"] + 1


class Player1(Player):
    def __init__(self, name=input("What is your name? ").upper()):
        self.name = name
        Player.__init__(self, name)


class Player2(Player):
    def __init__(self, name="ENEMY"):
        Player.__init__(self, name)

    def __repr__(self):
        return self.name








