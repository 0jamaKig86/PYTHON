import math


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True
def solve(a,k,n): # binh phuong co lap
    b = 1
    K = (str(bin(k))[2:])[::-1]
    if k == 0:
        return b
    A =a
    if K[0] == '1':
        b = a 
    for i in range(1,len(K)):
        A = (A*A) % n
        if K[i] == '1':
            b = (A*b) % n
    
    return b

def smallerPrime(MSV):
    while True:
        if isPrime(MSV):
            return MSV
        MSV -= 1

def biggerPrime(MSV):
    while True:
        if isPrime(MSV):
            return MSV
        MSV += 1
def theNearestPrime(MSV):
    if MSV - smallerPrime(MSV) > biggerPrime(MSV) - MSV:
        return biggerPrime(MSV)
    else:
        return smallerPrime(MSV)
if __name__ == '__main__':
    MSV = int(input("Enter MSV = "))
    a = int(input("Enter SBD = "))
    k = theNearestPrime(MSV)
    print(solve(a,k,123456))

