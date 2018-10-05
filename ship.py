from ship_operations import take_ship_data, check_proximity
from board_operations import update_board, print_boards


available_directions = ["n", "s", "w", "e"]
coordinates_mapping = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}


class Ship(object):

    def __init__(self, name, health_points, size, quantity, ship_position, direction):
        """Ship's name is the one from available_ships dictionary."""

        self.name = name
        self.health_points = health_points
        self.size = size
        self.quantity = quantity
        self.ship_position = ship_position
        self.direction = direction

    @staticmethod
    def create_fleet(game, player, board_player, total_ships, available_ships):
        # game, game.player, game.board_player, game.board_enemy, total_ships, available_ships

        # game, game.enemy, game.board_enemy, game.board_player, total_ships, available_ships

        print(available_ships)

        # print("Total ships " + str(total_ships))

        total_ships = 1

        for i in range(total_ships):

            while len(player.fleet) < total_ships:
                print("Creating fleet for " + player.name)
                ship_data = take_ship_data(available_ships,
                                           coordinates_mapping,
                                           available_directions)

                name = ship_data[0]
                health_points = ship_data[1]
                size = health_points
                quantity = ship_data[2]
                ship_position = ship_data[3]
                direction = ship_data[4]

                if name == "battleship" and available_ships[name][0] > 0:
                    ship = Ship.create_battleship(name,
                                                  health_points,
                                                  size, quantity,
                                                  ship_position,
                                                  direction)
                    if len(player.fleet) == 0:
                        player.fleet.append(ship)
                        available_ships[name][0] -= 1
                    else:
                        if check_proximity(ship_position[0],
                                           ship_position[1],
                                           size,
                                           direction,
                                           coordinates_mapping,
                                           board_player.board):
                            player.fleet.append(ship)
                            available_ships[name][0] -= 1

                if name == "cruiser" and available_ships[name][0] > 0:
                    ship = Ship.create_cruiser(name, health_points,
                                               size,
                                               quantity,
                                               ship_position,
                                               direction)
                    if len(player.fleet) == 0:
                        player.fleet.append(ship)
                        available_ships[name][0] -= 1
                    else:
                        if check_proximity(ship_position[0],
                                           ship_position[1],
                                           size, direction,
                                           coordinates_mapping,
                                           board_player.board):
                            player.fleet.append(ship)
                            available_ships[name][0] -= 1

                if name == "destroyer" and available_ships[name][0] > 0:
                    ship = Ship.create_destroyer(name,
                                                 health_points,
                                                 size, quantity,
                                                 ship_position,
                                                 direction)
                    if len(player.fleet) == 0:
                        player.fleet.append(ship)
                        available_ships[name][0] -= 1
                    else:
                        if check_proximity(ship_position[0],
                                           ship_position[1],
                                           size, direction,
                                           coordinates_mapping,
                                           board_player.board):
                            player.fleet.append(ship)
                            available_ships[name][0] -= 1

                if name == "submarine" and available_ships[name][0] > 0:
                    ship = Ship.create_submarine(name,
                                                 health_points,
                                                 size,
                                                 quantity,
                                                 ship_position,
                                                 direction)
                    if len(player.fleet) == 0:
                        player.fleet.append(ship)
                        available_ships[name][0] -= 1
                    else:
                        if check_proximity(ship_position[0],
                                           ship_position[1],
                                           size,
                                           direction,
                                           coordinates_mapping,
                                           board_player.board):
                            player.fleet.append(ship)
                            available_ships[name][0] -= 1

                board_player = update_board(board_player,
                                            player.fleet,
                                            coordinates_mapping)
                print("Updated board " + player.name)
                print_boards(game, player, board_player, game.enemy.name, game.empty_board_enemy)

    @classmethod
    def create_battleship(cls, name, health_points, size, quantity, ship_position, direction):
        ship = Battleship(name,
                          health_points,
                          size,
                          quantity,
                          ship_position,
                          direction)
        return ship

    @classmethod
    def create_cruiser(cls, name, health_points, size, quantity, ship_position, direction):
        ship = Cruiser(name,
                       health_points,
                       size,
                       quantity,
                       ship_position,
                       direction)
        return ship

    @classmethod
    def create_destroyer(cls, name, health_points, size, quantity, ship_position, direction):
        ship = Destroyer(name,
                         health_points,
                         size,
                         quantity,
                         ship_position,
                         direction)
        return ship

    @classmethod
    def create_submarine(cls, name, health_points, size, quantity, ship_position, direction):
        ship = Submarine(name,
                         health_points,
                         size, quantity,
                         ship_position,
                         direction)
        return ship

    def __repr__(self):
        """Prints a string representation of an object."""
        ship_data = "Name: " + self.name.capitalize() + \
                    "\n" + "Health points: " + str(self.health_points) + \
                    "\n" + "Position: " + str(self.ship_position[0]) + str(self.ship_position[1].capitalize()) + \
                    "\n" + "Direction: " + self.direction.capitalize()
        return ship_data


class Battleship(Ship):
    def __init__(self, name, health_points, size, quantity, ship_position, direction):
        Ship.__init__(self, name, health_points, size, quantity, ship_position, direction)


class Cruiser(Ship):
    def __init__(self, name, health_points, size, quantity, ship_position, direction):
        Ship.__init__(self, name, health_points, size, quantity, ship_position, direction)


class Destroyer(Ship):
    def __init__(self, name, health_points, size, quantity, ship_position, direction):
        Ship.__init__(self, name, health_points, size, quantity, ship_position, direction)


class Submarine(Ship):
    def __init__(self, name, health_points, size, quantity, ship_position, direction):
        Ship.__init__(self, name, health_points, size, quantity, ship_position, direction)













