def main():
    strings_list = get_strings()
    print("You have entered:")
    for i in strings_list:
        print(i)
    print(f"In the list you have previously insert there are: [{count_vowels(strings_list)}] vowels.")


def get_strings():
    list = []
    to_add = input("Type a string ('aaa' to end): ")
    while to_add != 'aaa':
        list.append(to_add)
        to_add = input("Type a string ('aaa' to end): ")

    
    return list


def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    new = ''.join(s)
    
    for i in range(len(new)):
        if new[i] in vowels:
            count += 1
    
    return count


if __name__ == '__main__':
    main()