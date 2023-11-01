import random

# Global variables (Try to make score system count number of ships)
GRID = [[]]
GRID_SIZE = 10
SIZE_OF_SHIPS = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
NUM_OF_SHIPS = 10
SHIP_POSITIONS = [[]]
# NUM_OF_SHIPS_SUNK (Use this if you can make program track ships else use NUM_OF_HITS to win (20 hits to win))



print("Welcome to Battleships!")
print("Your objective is to the sink the enemy fleet!\n")

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
        grid.append(row)

    num_of_ships_placed = 0

    SHIP_POSITIONS []
    
    while num_of_ships_placed != NUM_OF_SHIPS:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0 cols -1 )
        direction = random.choice(["up", "down", "left", "right"])
        ship_size = SIZE_OF_SHIPS[0]
    pass


def place_ships():
    """
    Function to place ships on respective boards (player/cpu)
    - Should not print location as cpu board needs to be hidden
    - Import ships from list to get correct sizes?
    - Make sure ship placemenet cant overlap
    - 10 ships (1, 1, 1, 1, 2, 2, 2, 3, 3, 4)
    """
    pass


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


