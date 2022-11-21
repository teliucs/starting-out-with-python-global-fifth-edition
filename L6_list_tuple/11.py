# 11. Lo Shu Magic Square
# The Lo Shu Magic Square is a grid with 3 rows and 3 columns, shown in Figure 7-21. The  Lo Shu Magic Square has the following properties:
    # • The grid contains the numbers 1 through 9 exactly.
    # • The sum of each row, each column, and each diagonal all add up to the same number. 
# This is shown in Figure 7-22.
# In a program you can simulate a magic square using a two-dimensional list. Write a function that accepts a two-dimensional list as an argument and determines whether the list is a Lo Shu Magic Square. Test the function in a program.


def main():
    m = get_matrix()
    print("Your matrix is:")
    for rows in m:
        print(rows)
    print()
    
    r1, r2, r3 = sum_rows(m)
    c1, c2, c3 = sum_col(m)
    d1, d2 = sum_diagonal(m)
    
    if r1 == r2 == r3 == c1 == c2 == c3 == d1 == d2:
        print("The matrix above is a Lo Shu Magic Square.")
    else:
        print("The matrix above a Lo Shu Magic Square.")


def get_matrix():
    matrix = [[0 for _ in range(3)] for _ in range(3)]
    user_numbers = []
    
    index = 0
    while index < 9:
        value = int(input("Enter a number from 1 through 9: "))
        if value >=1 and value <= 9 and value not in user_numbers:
            print("Success")
            user_numbers.append(value)
            index += 1
        else:
            print("Your number is already entered or it is not in range 1-9. Please enter again.")
    
    index_2 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = user_numbers[index_2]
            index_2 += 1
    print()
    return matrix


def sum_rows(m):
    row_1 = 0
    for i in range(len(m)):
        row_1 += m[0][i]
    
    row_2 = 0
    for i in range(len(m)):
        row_2 += m[1][i]
        
    row_3 = 0
    for i in range(len(m)):
        row_3 += m[2][i]
    
    return row_1, row_2, row_3


def sum_col(m):
    col_1 = 0
    for i in range(len(m)):
        col_1 += m[i][0]

    col_2 = 0
    for i in range(len(m)):
        col_2 += m[i][1]

    col_3 = 0
    for i in range(len(m)):
        col_3 += m[i][2]
    
    return col_1, col_2, col_3


def sum_diagonal(m):
    diagonal_1 = 0
    for i in range(len(m)):
        diagonal_1 += m[i][i]
        
    diagonal_2 = 0
    for i in range(len(m)):
        diagonal_2 += m[i][len(m) - i -1]
    
    return diagonal_1, diagonal_2


if __name__ == '__main__':
    main()
