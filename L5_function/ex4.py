# Dr. Kimura would like a program that he can use to simulate ten coin tosses, one after the other. Each time the program simulates a coin toss, it should randomly display either “Heads” or “Tails”.

# Algorithm:
    # Repeat 10 times:
        # If a random number in the range of 1 through 2 equals 1 then:
            # Display ‘Heads’
        # Else:
            # Display ‘Tails’

import random

# HEAD = 1
# TAIL = 2
# TOSSES = 10
            
def main():
    for toss in range(10):
        if random.randint(1, 2) == 1:
            print(f"For the {toss + 1} time you get HEAD")
        else:
            print(f"For the {toss + 1} time you get TAIL")

main()