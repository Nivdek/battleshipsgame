
import random

# Global variables (Try to make score system count number of ships)
GRID = [[]]
GRID_SIZE = 10
SIZE_OF_SHIPS = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
NUM_OF_SHIPS = 10
SHIP_POSITIONS = [[]]
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM_OF_SHIPS_SUNK = 0


def place_ships(start_row, end_row, start_col, end_col):
    """
    Checks the row and column values to make sure they are not already occupied
    """
    global GRID
    global SHIP_POSITIONS

    all_valid = True
    # for loop makes sure all the cells where a ship is trying to be placed is equal to Water
    for row in range(start_row, end_row):
        for column in range(start_col, end_col):
            if GRID[row][column] != "~":
                all_valid = False
                break
    # if condition updates the value of the grids cells to O if a ship was succesfully placed there
    if all_valid:
        SHIP_POSITIONS.append([start_row, end_row, start_col, end_col])
        for row in range(start_row, end_row):
            for column in range(start_col, end_col):
                GRID[row][column] = "O"
    return all_valid


def try_to_place_ships(row, col, direction, length):
    """
    Function will try designate a location within the grid for a ship using a helper method to make sure the location is not already occupied.
    It makes sure all ships have their starting and ending positional values stay within the confines of the defined grid size.
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
    # Creates a grid and assigns the games symbol for Water as a value to them
    rows, cols = (GRID_SIZE, GRID_SIZE)
    GRID = []
    for row in range(rows):
        row = []
        for column in range(cols):
            row.append("~")
        GRID.append(row)

    num_of_ships_placed = 0
    # While loop to place as many ships as are stated in the NUM_OF_SHIPS variable. meant to be defined at game start.
    while num_of_ships_placed != NUM_OF_SHIPS:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        # This uses the SIZE_OF_SHIPS list to determine size of ships, this is meant to be determined at the start of the game.
        ship_size = SIZE_OF_SHIPS[num_of_ships_placed]
        # Uses try_to_place_ships to make sure ships are placed inside of the grid and do not overlap.
        if try_to_place_ships(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1


def print_grid():
    """
    Prints the grid with letters representing rows and numbers representing columns
    """
    global GRID
    global ALPHABET

    debug_mode = True

    ALPHABET = ALPHABET[0: len(GRID) + 1]
    # for loop to apped a letter infront of every row of the grid.
    for row in range(len(GRID)):
        print(ALPHABET[row], end=") ")
        for col in range(len(GRID[row])):
            if GRID[row][col] == "O":
                # this debug feature lets you just debug_mode to true in order to see the positions of ships printed on the board.
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


def valid_format(placement):
    return len(placement) == 2

def valid_row(row, GRID_SIZE):
    return 0 <= row < GRID_SIZE

def valid col(col, GRID_SIZE):
    return 0 <= col < GRID_SIZE


def shot_placement():
    """
    Contains input for where the player wants to shoot and also handles any faulty input attempts.
    """
    global ALPHABET
    global GRID

    valid_placement = False
    row, col = -1, -1


    # While loop to make sure user inputs the correct format for his shot, transforms input to uppercase to match the values of ALPHABET.
    while not valid_placement:
        placement = input("Pick a square to bomb, such as C7 or D5: ")
        if not valid_format(placement):
            print("Please use the correct format, such as C7 or D5.")
            continue
        row, col = ALPHABET.find(placement[0]), int(placement[1])
        if not (row.isalpha() and valid_row(row, GRID_SIZE) and valid_col(col, GRID_SIZE)):
            print("Incorrect row or column.")
            continue
        if GRID[row][col] in {"#", "X"}:
            print("You have already bombed this location, pick another one!")
            continue
        elif GRID[row][col] == "~" or GRID[row][col] == "0":
            valid_placement = True

    return row, col

def sunk_ships():
    """
    Contains a check to see if a ship has been sunk.
    """


def print_shot():
    """
    Prints the placement of your shot on the board.
    """


def main():
    create_grid()
    print("X = Hit. @ = Miss. ~ = ?\n______________________")
    print_grid()
    print("Welcome to Battleships.\nYour objective is to sink the enemy fleet.")
    print(SHIP_POSITIONS)
    shot_placement()
main()