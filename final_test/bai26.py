import math


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True

if __name__ == '__main__':
    n = int(input("Enter N = "))
    for x in range(n ):
        for i in range(1, int(math.sqrt(x)) +1):
            if isPrime(i) and x % i == 0 \
                    and x % (i * i) == 0:
                print(x, end=", ")
    