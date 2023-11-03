import random

GRID = [[]]
GRID_SIZE = 10
NUM_OF_SHIPS = 10
SHIP_POSITIONS = []
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SIZE_OF_SHIPS = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]



def create_grid():
    """
    Function creates a 10x10 GRID and places 10 ships of predetermined sizes in a random fashion on said GRID.
    """
    global GRID
    global GRID_SIZE
    global NUM_OF_SHIPS
    global SHIP_POSITIONS
    global SIZE_OF_SHIPS

    random.seed()

    rows, cols = (GRID_SIZE, GRID_SIZE)

    GRID = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append("~")
        GRID.append(row)

    num_of_ships_placed = 0

    while num_of_ships_placed != NUM_OF_SHIPS:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = SIZE_OF_SHIPS[num_of_ships_placed]
        if try_to_place_ships(random_row, random_col, direction, ship_size):
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
            if GRID[r][c] != ".":
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
    Function will try designate a location within the GRID for a ship using a helper method to make sure the location is not already occupied
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


def print_grid():
    """
    Prints the GRID with letters representing rows and numbers representing columns
    """
    global GRID
    global ALPHABET

    debug_mode = True

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


def main():
    create_grid()
    print_grid()

main()