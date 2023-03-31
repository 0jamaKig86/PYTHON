import math


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True


def F(n):
    if isPrime(n):
        return n
    else:
        return 0


if __name__ == '__main__':
    L = int(input("Enter L = "))
    R = int(input("Enter R = "))
    sum = 0
    for i in range(L, R+1, 1):

        for j in range(i+1, R+1, 1):

            sum += F(i) * F(j)
    print(sum)
