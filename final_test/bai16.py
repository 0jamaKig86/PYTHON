import math
import random


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True


def randomNumberList(n):
    random_list = []
    for i in range(n):
        random_list.append(random.randint(0, 1000))

    return random_list


if __name__ == '__main__':
    n = int(input("Enter N = "))
    random_list = randomNumberList(n)
    print("The random list : ", random_list)
    print("\nThe prime of random list: ")
    for i in random_list:
        if isPrime(i):
            print(i, end=", ")
