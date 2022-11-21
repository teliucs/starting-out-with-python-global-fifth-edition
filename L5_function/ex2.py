# Your friend Michael runs a catering company. Some of the ingredients that his recipes require are measured in cups. When he goes to the grocery store to buy those ingredients, however, they are sold only by the fluid ounce. He has asked you to write a simple program that converts cups to fluid ounces.

# Algorithm:
    # Display an introductory screen that explains what the program does.
    # Get the number of cups.
    # Convert the number of cups to fluid ounces and display the result. (1 cup = 8 fluid ounces)
    
def main():
    introduction_screen()
    cups_needed = int(input("Type here the number of cups: "))
    convert(cups_needed)

def introduction_screen():
    print('This program converts measurements') 
    print('in cups to fluid ounces. For your') 
    print('reference the formula is:') 
    print(' 1 cup = 8 fluid ounces') 
    print()

def convert(cups_needed):
    ounces = cups_needed * 8
    print(f'That converts to {ounces} ounces.')
main()