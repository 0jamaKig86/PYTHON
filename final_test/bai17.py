import math


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True

def searchX(n, A, B, C):
    for x in range(1, n + 1):
        expr = A * x * x + B * x + C
        if isPrime(expr):
            return x
    
    return None
    


if __name__ == '__main__':
    n = int(input("Enter N = "))
    A = int(input("Enter A = "))
    B = int(input("Enter B = "))
    C = int(input("Enter C = "))
    result = searchX(n,A,B,C)
    if result != None :
        print("X = ",searchX(n,A,B,C))
    else:
        print("X not exist!!!")

