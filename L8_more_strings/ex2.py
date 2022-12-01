# At the university, passwords for the campus computer system must meet the following requirements:

# The password must be at least seven characters long.
# It must contain at least one uppercase letter
# t must contain at least one lowercase letter.
# It must contain at least one numeric digit.
# When a student sets up his or her password, the password must be validated to ensure it meets these requirements. You have been asked to write the code that performs this validation.

# I have added two more checks: special characters and two consecutive characters.


def main():
    print("Let me check your password")
    password = input("Type here your password:\n")
    
    while not check_psw(password):
        print("You have to modify your password.")
        password = input("Type here your password:\n")

    else:
        print("Your password is correct.")


def check_psw(psw):
    good = True
    
    if len(psw) <= 6 :
        good = False
       
    if not any(char.isupper() for char in psw):
        good = False
        
    if not any(char.islower() for char in psw):
        good = False
    
    if not any(char.isdigit() for char in psw):
        good = False
    
    special_characters = "!@#$%^&*()-+?_=,<>/"
    if not any(c in special_characters for c in psw):
        good = False
        
    for i in range(len(psw)-1):
        if psw[i] == psw[i+1]:
            good = False
    
    return good


if __name__ == '__main__':
    main()