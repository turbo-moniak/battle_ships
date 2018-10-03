from ship import Ship
from board_operations import print_boards


def start_game(game):
    available_ships = {"battleship": [1, 4], "cruiser": [2, 3], "destroyer": [3, 2], "submarine": [4, 1]}
    total_ships = calculate_total_ships(available_ships)

    print_boards(game.board_player, game.empty_board_player, game.player.name, game.enemy.name)

    """Creates Player's fleet"""
    Ship.create_fleet(game.board_player,
                      game.player.name,
                      game.player.fleet,
                      game.empty_board_player,
                      total_ships,
                      available_ships,
                      game.enemy.name)
    available_ships = {"battleship": [1, 4], "cruiser": [2, 3], "destroyer": [3, 2], "submarine": [4, 1]}
    total_ships = calculate_total_ships(available_ships)

    """Creates Enemy's fleet"""
    game.enemy.name = input("What is your name? ").upper()
    print_boards(game.board_enemy, game.empty_board_enemy, game.enemy.name, game.player.name)
    Ship.create_fleet(game.board_enemy,
                      game.enemy.name,
                      game.enemy.fleet,
                      game.empty_board_enemy,
                      total_ships,
                      available_ships,
                      game.player.name)


def sink_ships(game, coordinates_mapping):
    available_ships = {"battleship": [1, 4], "cruiser": [2, 3], "destroyer": [3, 2], "submarine": [4, 1]}

    sunken_ships_player = calculate_sunken_ships(game.player.sunken_ships)
    sunken_ships_enemy = calculate_sunken_ships(game.enemy.sunken_ships)

    total_ships = calculate_total_ships(available_ships)

    while sunken_ships_player < total_ships or sunken_ships_enemy < total_ships:
        bomb_your_enemy(game.player.name,
                        game.empty_board_player,
                        game.enemy.name,
                        game.board_enemy,
                        coordinates_mapping)

    was_hit = True

    while was_hit:
        print(game.enemy.name + "'s turn")

        print_boards(game.board_enemy, game.empty_board_enemy, game.enemy.name, game.player.name)

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
        print_boards(game.board_enemy, game.empty_board_enemy, game.enemy.name, game.player.name)


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


def bomb_your_enemy(player_name, player_board, player_empty_board, enemy_name, enemy_board, coordinates_mapping):

    #player_name
    #player_board
    #player_empty_board
    #enemy_name
    #enemy_board
    was_hit = True
    while was_hit:

        print(player_name + "'s turn")

        print_boards(player_board, player_empty_board, player_name, enemy_name)

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
            player_board[x][y] = " X "
            check_if_sunken(x, y, enemy_board)
        else:
            was_hit = False
        print_boards(player_board, player_empty_board, player_name, enemy_name)



