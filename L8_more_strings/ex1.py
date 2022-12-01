# At a university, each student is assigned a system login name, which the student uses to log into the campus computer system. You have been asked to write the code that generates system login names for students.

# Algorithm:
# Get the first three characters of the student’s first name. (If the first name is less than three characters in length, use the entire first name.)
# Get the first three characters of the student’s last name. (If the last name is less than three characters in length, use the entire last name.)
# Get the last three characters of the student’s ID number. (If the ID number is less than three characters in length, use the entire ID number.)
# Concatenate the three sets of characters to generate the login name.
# For example, if a student’s name is Amanda Spencer, and her ID number is ENG6721, her login name would be AmaSpe721.


def main():
    print("Hi welcome to your University")
    print("Here you can get your credentials to login.")
    
    name = input("Typer here your name:\n")
    surname = input("Typer here your surname:\n")
    id_number = input("Typer here your id:\n")
    
    print(f"Your credentials to login are: {get_name(name)}{get_name(surname)}{get_id(id_number)}.")


def get_name(string):
    return string[:3]


def get_id(int):
    return int[-3:]


if __name__ == '__main__':
    main()