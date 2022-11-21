# 10. Golf Scores
# The Springfork Amateur Golf Club has a tournament every weekend. The club president
# has asked you to write two programs:
    # 1. A program that will read each player’s name and golf score as keyboard input, then
    # save these as records in a file named golf.txt. (Each record will have a field for the player’s name and a field for the player’s score.)
    # 2. A program that reads the records from the golf.txt file and displays them.

def main():
    print("Hi Golf Player, I will save your tournament data.")
    print("Let's begin.")
    
    first_choice = int(input("Do y want to record score or see all the records? (1 / 2): "))
    while first_choice != 1 and first_choice != 2:
        print("You need to insert '1' or '2'.")
        first_choice = int(input("Do y want to record score or see all the records? (1 / 2): "))
    if first_choice == 1:
        record_score()
        second_choice = input("Do y want also to see all the records? (Y/n): ")
        second_choice = second_choice.lower()
        if second_choice == 'y':
            print('Reading...')
            print('...')
            read_record()
        else:
            print("Se you for the next record.")
    if first_choice == 2:
        print('Reading...')
        print('...')
        read_record()
    

def record_score():
    opener = open('10_golf.txt', 'a')
    
    week = int(input("Which week is this? "))
    players = int(input(f"How many players in the week #{week}? "))
    opener.write(f'Week #{week}:\n')
    
    for i in range(1, players + 1):
        name = input(f"Enter the name of player #{i}: ")
        score = float(input(f"Enter '{name}' score: "))
        opener.write(f'- {name}')
        opener.write(f'\t{str(score)}\n')
    print("Scores written in the file '10_golf.txt'.")
    
    opener.close()


def read_record():
    opener = open('10_golf.txt', 'r')
    print(opener.read())
    opener.close()


if __name__ == '__main__':
    main()