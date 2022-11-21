# 13. Magic 8 Ball
# Write a program that simulates a Magic 8 Ball, which is a fortune-telling toy that displays a 
# random response to a yes or no question. In the student sample programs for this book, you 
# will find a text file named 8_ball_responses.txt. The file contains 12 responses, such 
# as “I don’t think so”, “Yes, of course!”, “I’m not sure”, and so forth. The program should 
# read the responses from the file into a list. It should prompt the user to ask a question, then 
# display one of the responses, randomly selected from the list. The program should repeat 
# until the user is ready to quit.

import random


def main():
    print("Welcome to Magic 8 Ball game.")
    answers = get_answers()
    play(answers)


def get_answers():
    try:
        with open('Esercizi/L6_list_tuple/13_8_ball_responses.txt', 'r') as f:
            list = []
            for _ in f:
                list.append(f.readline().rstrip('\n'))
            return list
    except IOError:
        print("No file in this directory.")


def play(list):
    while True:
        question = input("What is your question? ('n' to exit)\n")
        if question.lower() == 'n':  
            break
        print(random.sample(list, 1))
        print()


if __name__ == '__main__':
    main()