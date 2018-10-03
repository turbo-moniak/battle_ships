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


def check_board(width, height, row, col, board):

    for i in range(height):
        for j in range(width):
            if 1 <= row < 10 and 1 <= col < 10:
                print(row, col, board.board[row][col])
                if board.board[row][col] != "___":
                    return False
            col = col + 1
        row = row + 1
        col = col - width

    return True


def check_proximity(row, col, size, direction, coordinates_mapping, board, ):
    col = coordinates_mapping[col]

    result = True

    if direction == "n":
        print("direction N")
        row = row - size
        col = col - 1
        result = check_board(3, size + 2, row, col, board) #width, height
        if not result:
            print("Can't anchor your ship here, there is another one nearby.")
    if direction == "s":
        print("direction S")
        row = row - 1
        col = col - 1
        result = check_board(3, size + 2, row, col, board) #width, height
        if not result:
            print("Can't anchor your ship here, there is another one nearby.")
    if direction == "w":
        row = row - 1
        col = col - size
        result = check_board(size + 2, 3, row, col, board) #width, height
        if not result:
            print("Can't anchor your ship here, there is another one nearby.")
    if direction == "e":
        row = row - 1
        col = col - 1
        result = check_board(size + 2, 3, row, col, board) #width, height
        if not result:
            print("Can't anchor your ship here, there is another one nearby.")

    return result







