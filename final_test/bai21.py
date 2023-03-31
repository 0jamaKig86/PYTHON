import math


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True

def isSuperPrime(n):
    count = 0
    for i in range(n):
        if isPrime(i):
            count+=1
    if isPrime(count):
        return True
    else:
        return False
    
if __name__ == '__main__':

    A = int(input("Enter A = "))
    B = int(input("Enter B = "))
    for i in range(A,B,1):
        if isSuperPrime(i):
            print(i,end=", ")

