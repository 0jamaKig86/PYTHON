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
def randomE(phiN):
    while True:
        e = random.randint(2,phiN)
        if math.gcd(e,phiN) == 1:
            return e
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
def searchD(e,phiN):
    if phiN == 0:
        x = 1
        return x
    b1 = phiN
    x2 = 1
    x1 = 0
    while phiN > 0:
        q = e // phiN
        r = e - q * phiN
        x = x2 - q * x1
        e = phiN
        phiN = r
        x2 = x1
        x1 = x
    x = x2
    return (x + b1) % b1
if __name__ == '__main__':
    for i in range(100,500):
        if isPrime(i):
            prime.append(i)
    p = random.choice(prime)
    q= random.choice(prime)
    n=p*q
    phiN = (p-1)*(q-1)
    e=randomE(phiN)

    d =searchD(e,phiN)
    sbd = int(input("Enter SBD = "))
    m = sbd + 123
    print(m)
    c =solve(m,e,n)
    print("C :",end=" ")
    print(c)
    m = solve(c,d,n)
    print(m)

    
