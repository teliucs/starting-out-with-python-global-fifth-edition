# World Series Winners


def main():
    winners = get_winners()
    choice = input("Which team do you want to check?\n")
    choice.lower()
    print(calculate_win(choice, winners))

def get_winners():
    try:
        with open('Esercizi/L6_list_tuple/10_WorldWinners.txt', 'r') as f:
            list = []
            for _ in f:
                team = f.readline().rstrip('\n').lower()
                list.append(team)
        return list
    except IOError:
        print("File not found in that directory.")


def calculate_win(team, list):
    counter = 0
    for i in range(len(list)):
        if list[i] == team:
            counter += 1
    
    return counter


def get_years(team, list):
    pass


if __name__ == '__main__':
    main()