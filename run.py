# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import time


def animation():
    animation = [
        "[        ]",
        "[=       ]",
        "[===     ]",
        "[====    ]",
        "[=====   ]",
        "[======  ]",
        "[======= ]",
        "[========]",
        "[ =======]",
        "[  ======]",
        "[   =====]",
        "[    ====]",
        "[     ===]",
        "[      ==]",
        "[       =]",
        "[        ]",
        "[        ]",
    ]

    notcomplete = True
    i = 0
    wait_time = random.randint(1, 4)
    timeout = time.time() + wait_time
    while notcomplete:
        print(animation[i % len(animation)], end="\r")
        time.sleep(0.1)
        i += 1
        if time.time() > timeout:
            break
    print()


# Define a class for the ships
class Ship:
    def __init__(self, name, size):
        # ship object has a name and size and cordinate and it check sinking status
        self.name = name
        self.size = size
        # List of coordinates occupied by the ship
        self.coords = []
        # Number of hits taken by the ship
        self.hits = 0

        def is_sunk(self):
        # Return True if the ship is sunk, False otherwise(return 0 for False and a number for True)
        return self.hits == self.size


# Define a class for the board
class Board:
    def __init__(self, size):
        # Size of the board
        self.size = size
        # Grid of cells
        # changing cell for diffrent cell character -- change line
        self.grid = [["." for _ in range(size)] for _ in range(size)]
        # List of ships on the board
        self.ships = []
        # Number of shots fired on the board
        self.shots = 0

        def print_board(self, show_ships):
        # Print the board with row and column labels
        # If show_ships is True, show the ships as "O", otherwise hide them as "."
        # Space for row labels
        print("  ", end="")
        for i in range(self.size):
            # Column labels
            # If the number on the clowmn label is equal to the grid size print it
            if i + 1 == self.size:
                print(i + 1, end=" ")
            else:
                # If column number has two digits, don't show it
                if len(str(i + 1)) != 2:
                    print(i + 1, end=" ")
                # Show 10 in the column number
                elif i == 9:
                    print(i + 1, end=" ")
                # If the column has two digits print "-" instead
                else:
                    print("-", end=" ")

        print()
        for i in range(self.size):
            # Row labels
            print(chr(i + 65), end=" ")
            for j in range(self.size):
                if show_ships or self.grid[i][j] != "O":
                    # Show the cell value unless it is a hidden ship
                    print(self.grid[i][j], end=" ")
                # Hide the ship as "."
                else:
                    print(".", end=" ")
            print()

            def place_ship(self, ship):
        # Place a ship on the board randomly and update its coordinates
        while True:
            # Choose a random orientation (vertical or horizontal) and position
            orientation = random.choice(["vertical", "horizontal"])
            if orientation == "vertical":
                # Choose a valid row
                row = random.randint(0, self.size - ship.size)
                # Choose any column
                col = random.randint(0, self.size - 1)
                # Check if the cells are empty
                if all(self.grid[row + i][col] == "." for i in range(ship.size)):
                    # Place the ship and update its coordinates
                    for i in range(ship.size):
                        self.grid[row + i][col] = "O"
                        ship.coords.append((row + i, col))
                    # Break out of the loop
                    break
            # orientation == "horizontal"
            else:
                # Choose any row
                row = random.randint(0, self.size - 1)
                # Choose a valid column
                col = random.randint(0, self.size - ship.size)
                # Check if the cells are empty
                if all(self.grid[row][col + i] == "." for i in range(ship.size)):
                    # Place the ship and update its coordinates
                    for i in range(ship.size):
                        self.grid[row][col + i] = "O"
                        ship.coords.append((row, col + i))

                    break  # Break out of the loop

                def fire(self, row, col):
        # Fire a shot at a given cell and return True if it hits a ship, False otherwise
        # Increment the number of shots
        self.shots += 1
        # Hit a ship
        if self.grid[row][col] == "O":
            # Mark the cell as hit
            self.grid[row][col] = "X"
            print("Hit!")
            # Find which ship was hit
            for ship in self.ships:
                if (row, col) in ship.coords:
                    # Increment the number of hits for that ship
                    ship.hits += 1
                    # Check if the ship is sunk
                    if ship.is_sunk():
                        animation()
                        print(f"You sunk my {ship.name}!")
                    # Break out of the loop
                    break
            return True
        # Missed a ship
        else:
            # Mark the cell as missed
            self.grid[row][col] = "#"
            animation()
            print("Miss!")
            return False

            def all_sunk(self):
        # Return True if all ships are sunk, False otherwise
        return all(ship.is_sunk() for ship in self.ships)


# Define a class for the game
class Game:
    def __init__(self):
        # Size of the board chosen by the user
        self.board_size = 0
        # Board object for the player's ships
        self.player_board = None
        # Board object for the computer's ships
        self.computer_board = None