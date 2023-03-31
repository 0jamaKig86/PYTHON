import math
import string
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

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True
def isCamichael(i):
        for x in range(1, i):
            if math.gcd(x, i) == 1:
                if (solve(x, i - 1, i) != 1):
                    return False
        return True

if __name__ == '__main__':


    n = int(input("Enter N = "))
    for i in range(2, n):
        if isPrime(i) == False:
            if isCamichael(i):
                print(i,end=", ")
    
