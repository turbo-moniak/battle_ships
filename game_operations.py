from ship import Ship
from board_operations import print_boards


def start_game(game):
    available_ships = {"battleship": [1, 4], "cruiser": [2, 3], "destroyer": [3, 2], "submarine": [4, 1]}
    total_ships = calculate_total_ships(available_ships)

    """Creates Player's fleet"""
    print_boards(game.player, game.board_player, game.enemy, game.empty_board_player)
    Ship.create_fleet(game, game.player, game.board_player, total_ships, available_ships)

    available_ships = {"battleship": [1, 4], "cruiser": [2, 3], "destroyer": [3, 2], "submarine": [4, 1]}
    total_ships = calculate_total_ships(available_ships)

    """Creates Enemy's fleet"""
    game.enemy.name = input("What is your name? ").upper()
    print_boards(game.enemy, game.board_enemy, game.player.name, game.empty_board_enemy)
    Ship.create_fleet(game, game.enemy, game.board_enemy, total_ships, available_ships)


def take_aim(coordinates_mapping):
    try:
        x = int(input("Coordinate X for your bomb: "))
    except ValueError:
        x = input("Coordinate X is a number between 1-10. Try again: ")
    y = input("Coordinate Y for your bomb: ")
    while y not in coordinates_mapping:
        y = input("The Y coordinate for your bomb is a col between A-J. Try again: ")

    coordinates = [x, y]

    return coordinates


def bomb_your_enemy(game, bomber, enemy_board, coordinates_mapping, enemy_name, board_bomber, empty_bomber_board):

    was_hit = True

    while was_hit:

        print(bomber.name + "'s turn")
        print_boards(bomber, board_bomber, enemy_name, empty_bomber_board)

        coordinates = take_aim(coordinates_mapping)

        x = coordinates[0]
        y = coordinates_mapping[coordinates[1]]

        if enemy_board.board[x][y] == " X ":
            was_hit = True
            empty_bomber_board.board[x][y] = " X "
            enemy_board.board[x][y] = " O "
            check_if_sunken(x, y, enemy_board)
        else:
            empty_bomber_board.board[x][y] = " + "
            was_hit = False
            print_boards(bomber, board_bomber, enemy_name, empty_bomber_board)
            print()
            print()
            print(bomber.name + " you missed!")

    return was_hit


def sink_ships(game):
    available_ships = {"battleship": [1, 4], "cruiser": [2, 3], "destroyer": [3, 2], "submarine": [4, 1]}
    coordinates_mapping = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}

    sunken_ships_player = calculate_sunken_ships(game.player.sunken_ships)
    sunken_ships_enemy = calculate_sunken_ships(game.enemy.sunken_ships)

    total_ships = calculate_total_ships(available_ships)

    was_hit = bomb_your_enemy(game,
                              game.player,
                              game.board_enemy,
                              coordinates_mapping,
                              game.enemy.name,
                              game.board_player,
                              game.empty_board_player)

    while sunken_ships_player < total_ships or sunken_ships_enemy < total_ships:

        print("Was hit value is " + str(was_hit))

        if was_hit:
            was_hit = bomb_your_enemy(game,
                                      game.player,
                                      game.board_enemy,
                                      coordinates_mapping,
                                      game.enemy.name,
                                      game.board_player,
                                      game.empty_board_player)
        else:
            was_hit = bomb_your_enemy(game,
                                      game.enemy,
                                      game.board_player,
                                      coordinates_mapping,
                                      game.player.name,
                                      game.board_enemy,
                                      game.empty_board_enemy)


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
    print("not implemented yet")
    pass