import random

# Global variables
GRID = [[]]
GRID_SIZE = 10
SIZE_OF_SHIPS = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
NUM_OF_SHIPS = 10
SHIP_POSITIONS = [[]]
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM_OF_SHIPS_SUNK = 0
GAME_OVER = False


def place_ships(start_row, end_row, start_col, end_col):
    """
    Checks the row and column values to make sure
    they are not already occupied
    """
    global GRID
    global SHIP_POSITIONS

    all_valid = True
    # Makes sure ships don't overlap
    for row in range(start_row, end_row):
        for col in range(start_col, end_col):
            if GRID[row][col] != "~":
                all_valid = False
                break
    # Logs position of ships
    if all_valid:
        SHIP_POSITIONS.append([start_row, end_row, start_col, end_col])
        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                GRID[row][col] = "O"
    return all_valid


def try_to_place_ships(row, col, direction, length):
    """
    Function will try designate a location within the grid for a ship using a
    helper method to make sure the location is not already occupied.
    It makes sure all ships have their starting and ending positional
    values stay within the confines of the defined grid size.
    """
    global GRID_SIZE

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= GRID_SIZE:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= GRID_SIZE:
            return False
        end_row = row + length

    return place_ships(start_row, end_row, start_col, end_col)


def create_grid():
    """
    Function to create a 10x10 grid and randomly place ships.
    """
    global GRID
    global GRID_SIZE
    global NUM_OF_SHIPS
    global SHIP_POSITIONS
    global SIZE_OF_SHIPS

    random.seed()
    # Creates a grid
    rows, cols = (GRID_SIZE, GRID_SIZE)
    GRID = []
    for row in range(rows):
        row = []
        for column in range(cols):
            row.append("~")
        GRID.append(row)

    SHIP_POSITIONS = []
    num_of_ships_placed = 0
    # Place as many ships as are stated in the NUM_OF_SHIPS variable.
    while num_of_ships_placed != NUM_OF_SHIPS:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        # Uses the SIZE_OF_SHIPS list to determine sizes of ships.
        ship_size = SIZE_OF_SHIPS[num_of_ships_placed]
        # Makes sure ship's dont overlap.
        if try_to_place_ships(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1


def print_grid():
    """
    Prints the grid with letters representing rows
    and numbers representing columns
    """
    global GRID
    global ALPHABET

    debug_mode = False

    ALPHABET = ALPHABET[0: len(GRID) + 1]
    # for loop to append a letter infront of every row of the grid.
    for row in range(len(GRID)):
        print(ALPHABET[row], end=") ")
        for col in range(len(GRID[row])):
            if GRID[row][col] == "O":
                # When true the ship positions are visible.
                if debug_mode:
                    print("O", end=" ")
                else:
                    print("~", end=" ")
            else:
                print(GRID[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(GRID[0])):
        print(str(i), end=" ")
    print("")


def shot_placement():
    """
    Contains input for where the player wants to shoot
    and also handles any faulty input attempts.
    """
    global ALPHABET
    global GRID

    valid_placement = False
    row, col = -1, -1

    # Makes sure user gives correct input.
    while not valid_placement:
        placement = input("Pick a square to bomb, such as C7 or D5: ")
        placement = placement.upper()

        if len(placement) != 2:
            print("Please use the correct format, such as C7 or D5.")
            continue
        row, col = placement[0], placement[1]
        if not (row.isalpha() and col.isnumeric()):
            print("Please use the correct format, such as C7 or D5.")
            continue
        row = ALPHABET.find(row)
        col = int(col)
        if not (0 <= row < GRID_SIZE) or not (0 <= col < GRID_SIZE):
            print("Please use the correct format, such as C7 or D5.")
            continue
        if GRID[row][col] == "#" or GRID[row][col] == "X":
            print("You've already bombed this location. Choose a new target!")
            continue
        if GRID[row][col] == "~" or GRID[row][col] == "O":
            valid_placement = True

    return row, col


def sunk_ships(row, col):
    """
    Checks if all parts of a ship has been hit and if so
    returns True to be used for increasing the number of ships sunk.
    """
    global SHIP_POSITIONS
    global GRID

    for position in SHIP_POSITIONS:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if GRID[r][c] != "X":
                        return False
    return True


def print_shot():
    """
    Prints the placement of your shot on the board.
    """
    global GRID
    global NUM_OF_SHIPS_SUNK

    row, col = shot_placement()

    if GRID[row][col] == "~":
        print("No enemy in this location.")
        GRID[row][col] = "#"
    elif GRID[row][col] == "O":
        print("You hit an an enemy!", end=" ")
        GRID[row][col] = "X"
        if sunk_ships(row, col):
            print("The enemy sunk!")
            NUM_OF_SHIPS_SUNK += 1
        else:
            print("It damaged the enemy ship!")


def check_win():
    """
    Checks whether all enemy ships have been sunk and if so it's game over.
    """
    global NUM_OF_SHIPS_SUNK
    global NUM_OF_SHIPS
    global GAME_OVER

    if NUM_OF_SHIPS == NUM_OF_SHIPS_SUNK:
        print("The entire fleet has been wiped out. You are victorious!")
        GAME_OVER = True


def main():
    """
    Main application containing the game loop
    """
    print("Welcome to Battleships.\nYour mission is to sink the enemy fleet.")
    print("X = Hit. @ = Miss. ~ = ?\n______________________")
    create_grid()

    while GAME_OVER is False:
        print_grid()
        print(f"There are {NUM_OF_SHIPS - NUM_OF_SHIPS_SUNK} ships remaining.")
        print_shot()
        print("----------------------------------")
        check_win()


main()
