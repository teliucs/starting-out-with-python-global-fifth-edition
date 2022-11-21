# 4. Morse Code Converter
# Morse code is a code where each letter of the English alphabet, each digit, and various punctuation
# characters are represented by a series of dots and dashes. Table 8-4 shows part  of the code.
# Write a program that asks the user to enter a string, then converts that string to Morse code.

# Character     Code            Character Code          Character   Code        Character   Code
# space         space           6         – . . . .     G           – – .       Q           – – . –
# comma         – – . . – –     7         – – . . .     H           . . . .     R           . – .
# period        . – . – . –     8         – – – . .     I           . .         S           . . .
# q. m. (?)     . . – – . .     9         – – – – .     J           . – – –     T           –
# 0             – – – – –       A         . –           K           – . –       U           . . –
# 1             . – – – –       B         – . . .       L           . – . .     V           . . . –
# 2             . . – – –       C         – . – .       M           – –         W           . – –
# 3             . . . – –       D         – . .         N           – .         X           – . . –
# 4             . . . . –       E         .             O           – – –       Y           – . –
# 5             . . . . .       F         . . – .       P           . – – .     Z           – – . .


def main():
    
    user_input = input("Enter a string to be converted into morse code:\n")
    user_input = user_input.upper()
    
    user_input_list = list(user_input)
    print(user_input_list)
    
    converter(user_input_list)
    
    
def converter(txt):
    character=[" ", ",", ".", "?", "0", "1", "2", "3", "4", "5", "6", "7",\
               "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", \
               "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", \
               "W", "X", "Y", "Z"]
    morse=[" ", "--..--", ".-.-.-", "..--..", "-----", ".----", "..---", "...--", \
           "....-", ".....", "-....", "--...", "---..", "----.", ".-", "-...", "-.-.", \
           "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", \
           ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.-", "--.."]
    
    for i in range(len(txt)):
        position = character.index(txt[i])
        print(morse[position], end=" ")


if __name__ == '__main__':
    main()