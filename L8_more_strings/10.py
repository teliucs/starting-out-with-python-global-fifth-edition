# 10. Most Frequent Character
# Write a program that lets the user enter a string and displays the character that appears most
# frequently in the string.


def main():
    string = input("Enter here a string:\n")
    freq, most_freq_char, max_frenq = get_most_frequent(string)
    
    print(f"The most frquency character of '{string}' is '{most_freq_char}' with [{max_frenq}].")            
    #Displays the each character and their corresponding frequency
    for i in range(0, len(freq)):
        if(string[i] != ' ' and string[i] != '0'):
            print(f"[{string[i]}] ---> {freq[i]}")
            

def get_most_frequent(string):
    freq = [0] * len(string) 
    max_frenq = 0
        
    for i in range(0, len(string)):
        freq[i] = 1
        for j in range(i+1, len(string)):
            if(string[i] == string[j]):
                freq[i] = freq[i] + 1
                #Set string[j] to 0 to avoid printing visited character  
                string = string[ : j] + '0' + string[j+1 : ]
        if freq[i] > max_frenq:
            max_frenq = freq[i]
    
    max_index = freq.index(max(freq))
    most_freq_char = string[max_index]  
    
    return freq, most_freq_char, max_frenq


if __name__ == '__main__':
    main()