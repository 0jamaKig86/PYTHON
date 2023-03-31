import math


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1)):
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
if __name__ == '__main__':


    a = int(input('Enter a = '))
    k = int(input('Enter k = '))
    n = int(input("Enter n = "))
    b = solve(a, k, n)
   
    if (isPrime(b)):
        print("a^-1 mod p is a prime ")
    else:
        print("a^-1 mod p is not a prime ")
