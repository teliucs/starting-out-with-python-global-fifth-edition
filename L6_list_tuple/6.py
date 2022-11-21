# 6. Assume the names variable references a list of strings. Write code that determines
# whether 'Ruby' is in the names list. If it is, display the message 'Hello Ruby'.
# Otherwise, display the message 'No Ruby'.

def main():
    inizialize()
    string = get_list_string()
    ruby_or_not(string)
    
def inizialize():
    print("Add some string and I'll say you if Ruby is contained or not.")
    print("...")
    
def get_list_string():
    list = []
    add = input("Add a string to your list (0 to end): ")
    while add is not "0":
        list.append(add)
        add = input("Add a string to your list (0 to end): ")
    return list

def ruby_or_not(list):
    if 'Ruby' in list:
        print('Hello Ruby.')
    else:
        print('No Ruby.')


if __name__ == '__main__':
    main()