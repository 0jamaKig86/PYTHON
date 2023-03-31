import math

def enterArr():

    n = list(map(int, input("Array :").strip().split()))
    return n
def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True
if __name__ == '__main__':
    A = enterArr()
    for i in A:
        for j in A:
            if i <= j:
                if isPrime(math.gcd(i,j)):
                    print([i,j],end=", ")