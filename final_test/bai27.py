import math
def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True

if __name__ == '__main__':

    a =int(input('Enter A = '))
    b=int(input('Enter B = '))

    for i in range(a+1, b):
        for j in range(a+1, b):
            if i < j:
                if isPrime(math.gcd(i, j)):
                    print([i,j],end=" ")
        
