import math


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True


def checkCubic(n):
    for i in range(int(math.pow(n, 1/3))+2):
        if i**3 == n:
            return True

    return False


if __name__ == '__main__':

    for i in range(100, 1000, 1):
        if isPrime(i):
            if checkCubic(int(str(i)[::-1])):
                print(i, end=", ")
