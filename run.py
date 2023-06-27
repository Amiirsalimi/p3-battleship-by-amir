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