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


def bomb_your_enemy(coordinates_mapping, bomber, bomber_board, empty_bomber_board, enemy_name, enemy_board, sunken_ships):

    print(bomber.name + "'s turn")
    print_boards(bomber, bomber_board, enemy_name, empty_bomber_board)

    coordinates = take_aim(coordinates_mapping)

    x = coordinates[0]
    y = coordinates_mapping[coordinates[1]]

    if enemy_board.board[x][y] == " X ":
        was_hit = True
        empty_bomber_board.board[x][y] = " X "
        enemy_board.board[x][y] = " 0 "
        print_boards(bomber, bomber_board, enemy_name, empty_bomber_board)
        if was_hit:
            check_if_sunken(x, y, enemy_board, sunken_ships)

    else:
        was_hit = False
        empty_bomber_board.board[x][y] = " + "
        print_boards(bomber, bomber_board, enemy_name, empty_bomber_board)
        print()
        print(bomber.name + " you missed")

    return was_hit


def sink_ships(game):
    available_ships = {"battleship": [1, 4], "cruiser": [2, 3], "destroyer": [3, 2], "submarine": [4, 1]}
    coordinates_mapping = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}

    sunken_ships_player = calculate_sunken_ships(game.player.sunken_ships)
    sunken_ships_enemy = calculate_sunken_ships(game.enemy.sunken_ships)

    total_ships = calculate_total_ships(available_ships)

    player_turn = True

    while sunken_ships_player < total_ships or sunken_ships_enemy < total_ships:

        if player_turn:
            was_hit = bomb_your_enemy(coordinates_mapping,
                                      game.player,
                                      game.board_player,
                                      game.empty_board_player,
                                      game.enemy.name,
                                      game.board_enemy,
                                      sunken_ships_enemy)
        else:
            was_hit = bomb_your_enemy(coordinates_mapping,
                                      game.enemy,
                                      game.board_enemy,
                                      game.empty_board_enemy,
                                      game.player.name,
                                      game.board_player,
                                      sunken_ships_player)

        if not was_hit:
            player_turn = not player_turn


def calculate_total_ships(ships):
    """Calculates how many ships are available in the game for each user."""
    total_ships = 0
    for k, v in ships.items():
        total_ships = total_ships + v[0]
    return total_ships


def find_anchor(row, col, player_board):

    anchor = 0

    if player_board.board[row - 1][col] == " X ":
        width = 1
        height = 4
        direction = 1 # vertical
    else:
        width = 4
        height = 1
        direction = 0 #horizontal

    for i in range(width):
        for j in range(height):
            if player_board.board[row][col] == " X " or player_board.board[row][col] == " 0 ":
                row = row - 1
            else:
                anchor = row + 1

    return [direction, anchor]


def calculate_sunken_ships(ships):
    sunken_ships = sum(ships.values())
    return sunken_ships


def check_size(direction, anchor, player_board, col):

    size = 0

    if direction == 1: # vertical down
        for i in range(4):
            for j in range(1):
                if player_board.board[anchor][col] == " X " or player_board.board[anchor][col] == " 0 ":
                    size = size + 1
            anchor = anchor + 1

    return size


def check_hits(anchor, col, player_board, size, direction):

    hits = 0

    if direction == 1: # vertical down
        for i in range(size):
            for j in range(1):
                if player_board.board[anchor][col] == " 0 ":
                    hits = hits + 1
            anchor = anchor + 1

    return hits


def check_if_sunken(row, col, player_board, sunken_ships):

    data = find_anchor(row, col, player_board)
    direction = data[0]
    anchor = data[1]
    print("Anchor " + str(anchor))

    size = check_size(direction, anchor, player_board, col)
    hits = check_hits(anchor, col, player_board, size, direction)


    # direction == 1 vertical
    # direction == 0 horizontal













