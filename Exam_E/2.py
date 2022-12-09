import random

def main():
    number = int(input("Give me an integer: "))
    print(harmonic_sum(number))
    test_recursive()


def harmonic_sum(n):
    if n == 1:
        return 1
    else:
        return (1/n) + harmonic_sum(n-1)


def test_recursive():
    print()
    n = random.randint(10, 100)
    print(f"Now let me test the recursive function [{n}] times:")
    for i in range(1, n + 1):
        print(f"The harmonic sum of [{i}] is: {harmonic_sum(i)}.")

if __name__ == '__main__':
    main()