# 1. Initials
# Write a program that gets a string containing a person’s first, middle, and last names, and 
# displays their first, middle, and last initials. For example, if the user enters John William 
# Smith, the program should display J. W. S.


def main():
    name=get_name()
    
    name_separated=name.split()
    
    print("Your initials...")
    
    for ch in name_separated:
        print(ch[0], ".", sep='', end="")
        
    
def get_name():
    name=input("Enter your full name: ")
    return name


if __name__ == '__main__':
    main()