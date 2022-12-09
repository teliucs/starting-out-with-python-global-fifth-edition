def main():
    n = get_length()
    if n is not False:
        list = add_strigs(n)
        save_file(list)
    

def get_length():
    good = False
    while not good:
        try:
            integer = int(float(input("Enter a positive integer: ")))
            while integer <= 0:
                integer = int(input("Enter a positive integer: "))
            good = True
            return integer
        except ValueError:
            print("You have to insert an integer.")


def add_strigs(n):
    return [input("Add a string:\n") for _ in range(n)]


def save_file(l):
    with open('Exam_E/list_strings.txt', 'w') as f:
        for i in l:
            f.write(i + '\n')
    print("You can find your updated list in the file 'list_strings.txt'.")


if __name__ == '__main__':
    main()