import random

# Global variables (Try to make score system count number of ships)
GRID = [[]]
GRID_SIZE = 10
SIZE_OF_SHIPS = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
NUM_OF_SHIPS = 10
SHIP_POSITIONS = [[]]
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# NUM_OF_SHIPS_SUNK = 0 (Maybe use for score if can find way to do this)


def create_grid():
    """
    Function to create a 10x10 grid and randomly place ships. (Try to get ship_size to iterate through SIZE_OF_SHIPS else change ship_size to be a randomized value just like the rest)
    Going to need a separate function to check if placement of ships is valid
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

    SHIP_POSITIONS = []
    
    while num_of_ships_placed != NUM_OF_SHIPS:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols -1 )
        direction = random.choice(["up", "down", "left", "right"])
        ship_size = SIZE_OF_SHIPS[0] #Not sure how to iterate through this to pull the correct ship sizes  !!!!THIS FUNCTION NEEDS TO BE CHANGED BECAUSE THE COMPUTER CURRENTLY PLACES 10 4-LENGTH SHIPS
        if try_to_place_ships(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1
            ship_size[] += 1 # Unsure if this is the correct way to loop through ship sizes.



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
                    print(".", end=" ")
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

def print_cpu_board():
    """
    This function prints out the cpu board but keeps the placement of ships visually hidden
    Maybe make one "hidden" internal board to process data and print one board as a visual representation?
    """
    pass


def print_player_board():
    """
    This function prints out the player board with ship placement visible to the player
    Maybe make one "hidden" internal board to process data and print one board as a visual representation?
    """
    pass


def score_system():
    """
    This function should check if you hit a ship and both update the board visually and increase your internal score (when score/hits reach 20 you win OR track number of ships and when ships sunk = 10 game is won/lost)
    """
    pass



