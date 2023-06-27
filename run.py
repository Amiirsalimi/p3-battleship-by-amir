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