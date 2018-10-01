def create_board(size):

    """Creates a board of a certain size (n by n) with cordinates x (A, B, C, D, E, F, G, H, I, J)
        and y (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)."""

    letter = 65
    board = [["___"] * size for i in range(size)]

    for i in range(size):
        for j in range(size):
            if i == 0 and j == 0:
                board[i][j] = "  "
            elif j == 0 and 0 < i < 10:
                board[i][j] = str(i) + " "
            elif j == 0 and i > 9:
                board[i][j] = str(i)
            elif i == 0 and j > 0:
                board[i][j] = " " + chr(letter) + " "
                letter += 1
        letter = 65

    return board


def print_boards(own, enemy, player_name, enemy_name):

    """Prints a string representation of a board."""
    print()
    print(" " + str(player_name) + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(enemy_name))
    for i in range(own.size):
        if i == 0:
            print(" ".join(own.board[i]) + "\t\t\t\t\t\t\t" + " ".join(enemy.board[i]))
        else:
            print(" ".join(own.board[i]) + "\t\t\t\t\t\t\t" + " ".join(enemy.board[i]))
            print()


def place_north(row, col, size, board):
    """Places the ship towards North given first coordinates."""

    for i in range(size):
        board[row][col] = " X "
        row -= 1
    return board


def place_south(row, col, size, board):
    """Places the ship towards South given first coordinates."""

    for i in range(size):
        board[row][col] = " X "
        row += 1
    return board


def place_east(row, col, size, board):
    """Places the ship East given first coordinates."""

    for i in range(size):
        board[row][col] = " X "
        col += 1
    return board


def place_west(row, col, size, board):
    """Places the ship West given first coordinates."""

    for i in range(size):
        board[row][col] = " X "
        col -= 1
    return board


def update_board(board, fleet, coordinates_mapping):

    ship = fleet[len(fleet) - 1]
    if ship.direction == 'n':
        board = place_north(ship.ship_position[0], coordinates_mapping[ship.ship_position[1]], ship.size, board)
    elif ship.direction == 's':
        board = place_south(ship.ship_position[0], coordinates_mapping[ship.ship_position[1]], ship.size, board)
    elif ship.direction == 'w':
        board = place_west(ship.ship_position[0], coordinates_mapping[ship.ship_position[1]], ship.size, board)
    else:
        board = place_east(ship.ship_position[0], coordinates_mapping[ship.ship_position[1]], ship.size, board)

    return board


def there_is_ship_nearby_message(row, y_coordinates, col, i, j):
    print("Can't anchor your ship at " + str(row) + y_coordinates[col - 1].upper() +
          " there is another ship nearby at " + str(i) + y_coordinates[j - 1].upper())


def check_east(row, col, size, board, y_coordinates):
    for i in range(row - 1, row + 1):
        for j in range(col - 1, col + size + 1):
            if board.board[i][j] != "___":
                there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                return False
    return True


def check_proximity(row, col, size, direction, coordinates_mapping, board):
    col = coordinates_mapping[col]
    y_coordinates = sorted(coordinates_mapping.keys())

    if row == 1 and col == 1:
        if direction == 's':
            print("1. Checking row == 1 and col == 1 direction SOUTH")
            for i in range(row, row + size + 1):
                for j in range(col, col + 2):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == "n":
            print("1. Checking row == 1 and col == 1 direction NORTH")
            for i in range(row, row - size - 1, -1):
                for j in range(col, col + 2):
                    print(i, j)
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 'e':
            print("1. Checking row == 1 and col == 1 direction EAST")
            for i in range(row, row + 2):
                for j in range(col, col + size + 1):
                    print(i, j)
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 'w':
            print("1. Checking row == 1 and col == 1 direction WEST")
            for i in range (row, row + 1):
                for j in range(col, col - size - 1, -1):
                    print(i, j)
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False

    if row == 1 and 1 < col < 10:
        if direction == 'e' or direction == 'e':
            print("2. Checking row == 1 and 1 < col < 10 direction EAST")
            for i in range(row, row + 2):
                for j in range(col - 1, col + size + 1):
                    print(i, j)
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 'w':
            print("2. Checking row == 1 and 1 < col < 10 direction WEST")
            for i in range(row, row + 2):
                for j in range(col + 1, col - size - 1, -1):
                    print(i, j)
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 's':
            print("2. Checking row == 1 and 1 < col < 10 direction SOUTH")
            for i in range(row, row + size + 1):
                for j in range(col - 1, col + 2):
                    print(i, j)
                    if board.board[i][j] != "___":
                        print("Can't anchor your ship at " + str(row) + y_coordinates[col - 1].upper() +
                              " there is another ship nearby.")
                        return False
        elif direction == 'n':
            print("2. Checking row == 1 and 1 < col < 10 direction NORTH")
            for i in range(row + 2, row - 1, -1):
                for j in range(col - 1, col + 2):
                    print(i, j)
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False

    if row == 1 and col == 10:
        if direction == 'w':
            print("3. Checking row == 1 and col == 10 direction WEST")
            for i in range(row, row + 2):
                for j in range(col, col - 3, -1):
                    print(i, j)
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 'e':
            print("3. Checking row == 1 and col == 10 direction EAST")
            for i in range(row, row + 2):
                for j in range(col - 1, col + 1):
                    print(i, j)
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 's':
            print("3. Checking row == 1 and col == 10 direction SOUTH")
            for i in range(row, row + size + 1):
                for j in range(col, col - 2, -1):
                    print(i, j)
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 'n':
            print("3. Checking row == 1 and col == 10 direction NORTH")
            for i in range(row, row + size + 1):
                for j in range(col - 1, col + 2):
                    print(i, j)
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False

    if 10 > row > 1 == col:
        if direction == 'e':
            print("4. Checking 10 > row > 1 == col direction EAST")
            for i in range(row - 1, row + 2):
                for j in range(col, col + 2):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 'n':
            print("4. Checking 10 > row > 1 == col direction NORTH")
            for i in range(row + 1, row - size - 1, -1):
                for j in range(col, col + 2):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 's':
            print("4. Checking 10 > row > 1 == col direction SOUTH")
            for i in range(row - 1, row + size + 1):
                for j in range(col, col + 2):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 'w':
            print("4. Checking 10 > row > 1 == col direction WEST")
            for i in range(row - 1, row + 2):
                for j in range(col + 1, col - size - 1, -1):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
    if 1 < row < 10 and 1 < col < 10:
        if direction == 'e':
            print("5. Checking 1 < row < 10 and 1 < col < 10 direction EAST")
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + size):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 'w':
            print("5. Checking 1 < row < 10 and 1 < col < 10 direction WEST")
            for i in range(row - 1, row + 2):
                for j in range(col + 1, col - size, -1):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 'n':
            print("5. Checking 1 < row < 10 and 1 < col < 10 direction NORTH")
            for i in range(row + 1, row - size - 1, -1):
                for j in range(col - 1, col + 2):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 's':
            print("5. Checking 1 < row < 10 and 1 < col < 10 direction SOUTH")
            for i in range(row - 1, row + size + 1):
                for j in range(col - 1, col + 2):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
    if 1 < row < 10 and col == 10:
        if direction == 's':
            print("6. Checking 1 < row < 10 and col == 10 direction SOUTH")
            for i in range(row - 1, row + size + 1):
                for j in range(col - 1, col + 1):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 'n':
            print("6. Checking 1 < row < 10 and col == 10 direction NORTH")
            for i in range(row + 1, row - size - 1, -1):
                for j in range(col - 1, col + 1):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 'w':
            print("6. Checking 1 < row < 10 and col == 10 direction WEST")
            for i in range(row - 1, row + 2):
                for j in range(col, col - size - 1, -1):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 'e':
            print("6. Checking 1 < row < 10 and col == 10 direction EAST")
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + size):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False

    if row == 10 and col == 1:
        if direction == "n":
            print("7. Checking row == 10 and col == 1 direction NORTH")
            for i in range(row, row - size - 1, -1):
                for j in range(col, col + 2):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        if direction == 'e':
            print("7. Checking row == 10 and col == 1 direction EAST")
            for i in range(row, row - 2, -1):
                for j in range(col, col + size + 1):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        if direction == 's':
            print("7. Checking row == 10 and col == 1 direction SOUTH")
            for i in range(row - 1, row + size):
                for j in range(col, col + 3):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        if direction == 'w':
            print("7. Checking row == 10 and col == 1 direction WEST")
            for i in range(row, row - 2, -1):
                for j in range(col + 1, col - size, -1):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False

    if row == 10 and 1 < col < 10:
        if direction == 'n':
            print("8. Checking row == 10 and 1 < col < 10 direction NORTH")
            for i in range(row, row - size - 1, -1):
                for j in range(col - 1, col + 2):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 's':
            print("8. Checking row == 10 and 1 < col < 10 direction SOUTH")
            for i in range(row - 1, row + size):
                for j in range(col - 1, col + 2):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 'w':
            print("8. Checking row == 10 and 1 < col < 10 direction WEST")
            for i in range(row - 1, row + 1):
                for j in range(col + 1, col - size - 1, -1):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 'e':
            print("8. Checking row == 10 and 1 < col < 10 direction EAST")
            for i in range(row - 1, row + 1):
                for j in range(col - 1, col + size + 1):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
    if row == 10 and col == 10:
        if direction == 'n':
            print("9. Checking row == 10 and col == 10 direction NORTH")
            for i in range(row, row - size - 1, -1):
                for j in range(col - 1, col + 1):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 's':
            print("9. Checking row == 10 and col == 10 direction SOUTH")
            for i in range(row - 1, row  + 1):
                for j in range(col - 1, col + 1):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 'w':
            print("9. Checking row == 10 and col == 10 direction WEST")
            for i in range(row, row - 2):
                for j in range(col, col - size - 1, -1):
                    if board.board[i][j] != "___":
                        there_is_ship_nearby_message(row, y_coordinates, col, i, j)
                        return False
        elif direction == 'e':
            print("9. Checking row == 10 and col == 10 direction EAST")
            check_east(row, col, size, board, y_coordinates)
    return True





