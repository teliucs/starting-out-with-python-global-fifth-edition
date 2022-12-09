import random

def main():
    matrix = get_matrix()
    for rows in matrix:
        print(rows)
    
    print(f"The determinant of the previous matrix is: [{compute_determinant(matrix)}].")


def get_matrix():
    return [[random.randint(0, 10) for _ in range(2)] for _ in range(2)]


def compute_determinant(m):
    return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])


if __name__ == '__main__':
    main()