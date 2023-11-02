import random

# Global variables (Try to make score system count number of ships)
GRID = [[]]
GRID_SIZE = 10
NUM_OF_SHIPS = 10
SHIP_POSITIONS = [[]]
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# NUM_OF_SHIPS_SUNK = 0 (Maybe use for score if can find way to do this)


def create_grid():
    """
    Function creates a 10x10 grid and places 10 ships of predetermined sizes in a random fashion on said grid.
    """
    global GRID
    global GRID_SIZE
    global NUM_OF_SHIPS
    global SHIP_POSITIONS 

    random.seed()

    rows, cols = (GRID_SIZE, GRID_SIZE)

    GRID = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append("~")
        GRID.append(row)
    SHIP_POSITIONS = []
    num_of_ships_placed = 0

    size_of_ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    num_of_ships_placed = 0
    while num_of_ships_placed != len(size_of_ships):
        for ship_size in size_of_ships:
            placed = False
            while not placed:
                random_row = random.randint(0, rows - 1)
                random_col = random.randint(0, cols - 1)
                direction = random.choice(["up", "down", "left", "right"])
                if try_to_place_ships(random_row, random_col, direction, ship_size):
                    placed = True
                    num_of_ships_placed += 1


def place_ships(start_row, end_row, start_col, end_col):
    """
    Checks the row and column values to make sure they are not previously occupied
    """
    global GRID
    global SHIP_POSITIONS

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if GRID[r][c] != "~":
                all_valid = False
                break
    if all_valid:
        SHIP_POSITIONS.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                GRID[r][c] = "O"
    return all_valid


def try_to_place_ships(row, col, direction, length):
    """
    Function will try designate a location within the grid for a ship using a helper method to make sure the location is not already occupied
    """
    global GRID_SIZE

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1
    elif direction == "down":
        if row + length >= GRID_SIZE:
            return False
        end_row = row + length
    elif direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1
    elif direction == "right":
        if col + length >= GRID_SIZE:
            return False
        end_col = col + length
    return place_ships(start_row, end_row, start_col, end_col)


def print_grid():
    """
    Prints the grid with letters representing rows and numbers representing columns
    """
    


def print_cpu_board():
    """
    This function prints out the cpu board but keeps the placement of ships visually hidden
    Maybe make one "hidden" internal board to process data and print one board as a visual representation?
    """
    global GRID
    global ALPHABET

    create_grid()
    debug_mode = False

    ALPHABET = ALPHABET[0: len(GRID) + 1]

    for row in range(len(GRID)):
        print(ALPHABET[row], end=") ")
        for col in range(len(GRID[row])):
            if GRID[row][col] == "O":
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


def print_player_board():
    """
    This function prints out the player board with ship placement visible to the player
    Only one player board is needed as location of ships are to be shown.
    """
    global GRID
    global ALPHABET

    create_grid()

    ALPHABET = ALPHABET[0: len(GRID) + 1]

    for row in range(len(GRID)):
        print(ALPHABET[row], end=") ")
        for col in range(len(GRID[row])):
            if GRID[row][col] == "O":
                print("O", end=" ")
            else:
                print("~", end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(GRID[0])):
        print(str(i), end=" ")
    print("")


def score_system():
    """
    This function should check if you hit a ship and both update the board visually and increase your internal score (when score/hits reach 20 you win OR track number of ships and when ships sunk = 10 game is won/lost)
    """
    pass


def main():
    print_cpu_board()
    print("+-+-+-+-+-+-+-+-+-+-+-+")
    print_player_board()    

main()

