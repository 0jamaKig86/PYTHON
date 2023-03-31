import math
import random
prime=[]

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
    for i in range(1000):
        if isPrime(i):
            prime.append(i)
    p = random.choice(prime)
    q = random.choice(prime)
    print("a^p mod q is a prime with p =",p,"and q =",q)
    print("a :",end=" ")
    for i in range(100):
        if isPrime(solve(i,p,q)):
            print(i,end=", ")