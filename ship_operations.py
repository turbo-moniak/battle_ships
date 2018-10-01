from board_operations import check_proximity


def take_ship_data(available_ships, coordinates_mapping, available_directions):

    name = take_name(available_ships)
    health_points = set_health_points(name, available_ships)
    size = health_points
    quantity = set_quantity(name, available_ships)
    ship_position = set_position(coordinates_mapping)
    direction = set_direction(available_directions)
    direction_check_up = check_direction(direction, ship_position[0], coordinates_mapping[ship_position[1]], size)

    while not direction_check_up:
        print()
        print("Can't place your ship towards " + direction.upper() + ", there is not enough room.")
        print()
        name = take_name(available_ships)
        health_points = set_health_points(name, available_ships)
        size = health_points
        quantity = set_quantity(name, available_ships)
        ship_position = set_position(coordinates_mapping)
        direction = set_direction(available_directions)
        direction_check_up = check_direction(direction, ship_position[0], coordinates_mapping[ship_position[1]], size)

    ship_data = [name, size, quantity, ship_position, direction]

    return ship_data


def take_name(available_ships):

    name = input("Choose a ship to place on the board:\n" +
                 "Battleship x " + str(available_ships["battleship"][0]) + "\n" +
                 "Cruiser x " + str(available_ships["cruiser"][0]) + "\n" +
                 "Destroyer x " + str(available_ships["destroyer"][0]) + "\n" +
                 "Submarine x " + str(available_ships["submarine"][0]) + "\n" +
                 "Your ship: ").lower()

    while name not in available_ships:
        if name not in available_ships:
            print()
            print(name.upper() + " is not available. Try again!\n")
            name = input("Choose a ship to place on the board:\n" +
                         "Battleship x " + str(available_ships["battleship"][0]) + "\n" +
                         "Cruiser x " + str(available_ships["cruiser"][0]) + "\n" +
                         "Destroyer x " + str(available_ships["destroyer"][0]) + "\n" +
                         "Submarine x " + str(available_ships["submarine"][0]) + "\n" +
                         "Your ship: ").lower()
        elif available_ships[name][0] == 0:
            print()
            print("You don't have more " + name + "s to place. Choose a different ship.\n")

            name = input("Choose a ship to place on the board:\n" +
                         "Battleship x " + str(available_ships["battleship"][0]) + "\n" +
                         "Cruiser x " + str(available_ships["cruiser"][0]) + "\n" +
                         "Destroyer x " + str(available_ships["destroyer"][0]) + "\n" +
                         "Submarine x " + str(available_ships["submarine"][0]) + "\n" +
                         "Your ship: ").lower()

    return name


def set_health_points(name, available_ships):
    return available_ships[name][1]


def set_x_coordinate():
    """Takes an X coordinate from a player, evaluate the type of the coordinate."""
    try:
        x = int(input("Set the X coordinate for your ship. Row (1-10): "))
    except ValueError:
        print("The row in a number between 1-10.")
        x = int(input("Set the X coordinate for your ship. Row (1-10): "))
    while x < 1 or x > 10:
        try:
            x = int(input("Set the X coordinate for your ship. Row (1-10): "))
        except ValueError:
            print("The row is a number between 1-10.")
            x = int(input("Set the X coordinate for your ship. Row (1-10): "))
    return x


def set_y_coordinate():
    """Takes a Y coordinate from a player and checks if it is available."""
    y = input("Set the Y coordinate for your ship. Col (A-J)").lower()
    return y


def set_position(coordinates_mapping):
    """Takes X and Y and sets ship_position."""

    coordinate_x = set_x_coordinate()
    coordinate_y = set_y_coordinate()

    while coordinate_y not in coordinates_mapping:
        print("The col is a letter between A-J")
        coordinate_y = set_y_coordinate()

    return [coordinate_x, coordinate_y]


def set_direction(available_directions):

    direction = input("Set direction for the ship (N, S, E, W): ").lower()
    while direction not in available_directions:
        print("Sorry, there is no such direction. Try again!")
        direction = input("Set direction for the ship (N, S, E, W): ").lower()

    return direction


def check_direction(direction, row, col, ship_size):
    """Checks if the ship stays within the board with the given coordinates and direction. Function calls
        respective function for checking each of directions. The result of the check is True if the ship
        stays within the board with the given direction."""

    ship_direction = False

    if direction == 'n':
        ship_direction = check_north(row, ship_size)
    elif direction == 's':
        ship_direction = check_south(row, ship_size)
    elif direction == 'w':
        ship_direction = check_west(col, ship_size)
    elif direction == 'e':
        ship_direction = check_east(col, ship_size)

    return ship_direction


def check_north(row, ship_size):
    """Checks if the ship can be placed towards North from the given coordinates."""

    north = False

    if row - ship_size >= 0:
        north = True

    return north


def check_south(row, ship_size):
    """Checks if the ship can be placed towards South from the given coordinates."""

    south = False

    if row + ship_size <= 11:
        south = True

    return south


def check_west(col, ship_size):
    """Checks if the ship can be placed towards West from the given coordinates."""

    west = False

    if col - ship_size >= 0:
        west = True

    return west


def check_east(col, ship_size):
    """Checks if the ship can be placed towards East from the given coordinates."""

    east = False

    if col + ship_size <= 11:
        east = True

    return east


def set_ship_health_points(name, available_ships):
    """Sets ship's health points based on data in available ships dictionary."""
    return available_ships[name][1]


def set_quantity(name, available_ships):
    """Sets ship's quantity based on data in available ships dictionary."""
    return available_ships[name][0]







