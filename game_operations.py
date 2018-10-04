from ship import Ship
from board_operations import print_boards


def start_game(game):
    available_ships = {"battleship": [1, 4], "cruiser": [2, 3], "destroyer": [3, 2], "submarine": [4, 1]}
    total_ships = calculate_total_ships(available_ships)

    """Creates Player's fleet"""
    print_boards(game, game.player, game.board_player, game.enemy)
    Ship.create_fleet(game, game.player, game.board_player, total_ships, available_ships)

    available_ships = {"battleship": [1, 4], "cruiser": [2, 3], "destroyer": [3, 2], "submarine": [4, 1]}
    total_ships = calculate_total_ships(available_ships)

    """Creates Enemy's fleet"""
    game.enemy.name = input("What is your name? ").upper()
    print_boards(game, game.enemy, game.board_enemy, game.player.name)
    Ship.create_fleet(game, game.enemy, game.board_enemy, total_ships, available_ships)


def sink_ships(game):
    available_ships = {"battleship": [1, 4], "cruiser": [2, 3], "destroyer": [3, 2], "submarine": [4, 1]}
    coordinates_mapping = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}

    sunken_ships_player = calculate_sunken_ships(game.player.sunken_ships)
    sunken_ships_enemy = calculate_sunken_ships(game.enemy.sunken_ships)

    total_ships = calculate_total_ships(available_ships)

    while sunken_ships_player < total_ships or sunken_ships_enemy < total_ships:
        bomb_your_enemy(game, game.player.name)

        was_hit = True

        while was_hit:
            print(game.enemy.name + "'s turn")

            print_boards(game, game.enemy, game.board_player, game.player.name)

            try:
                x = int(input("Coordinate X for your bomb: "))
            except ValueError:
                x = input("Coordinate X is a number between 1-10. Try again: ")
            y = input("Coordinate Y for your bomb: ")
            while y not in coordinates_mapping:
                y = input("The Y coordinate for your bomb is a col between A-J. Try again: ")

            coordinates = [x, y]

            x = coordinates[0]
            y = coordinates_mapping[coordinates[1]]

            if game.board_player.board[x][y] == " X ":
                game.empty_board_enemy.board[x][y] = " X "
            else:
                was_hit = False
            print_boards(game, game.player, game.board_player, game.enemy)


def calculate_total_ships(ships):
    """Calculates how many ships are available in the game for each user."""
    total_ships = 0
    for k, v in ships.items():
        total_ships = total_ships + v[0]
    return total_ships


def calculate_sunken_ships(ships):
    sunken_ships = sum(ships.values())
    return sunken_ships


def check_if_sunken(x, y, board):
    pass


def bomb_your_enemy(game, player_name):
    coordinates_mapping = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}

    player_board = game.board_player.board
    empty_player_board = game.empty_board_player

    enemy_board = game.board_enemy.board

    was_hit = True
    while was_hit:

        print(player_name + "'s turn")

        print_boards(game, game.player, game.empty_board_enemy, game.enemy.name)

        try:
            x = int(input("Coordinate X for your bomb: "))
        except ValueError:
            x = input("Coordinate X is a number between 1-10. Try again: ")
        y = input("Coordinate Y for your bomb: ")
        while y not in coordinates_mapping:
            y = input("The Y coordinate for your bomb is a col between A-J. Try again: ")

        coordinates = [x, y]

        x = coordinates[0]
        y = coordinates_mapping[coordinates[1]]

        if enemy_board[x][y] == " X ":
            game.empty_board_enemy.board[x][y] = " X "
            check_if_sunken(x, y, enemy_board)
        else:
            was_hit = False
        print_boards(game, game.player, game.empty_board_enemy, game.enemy.name)



