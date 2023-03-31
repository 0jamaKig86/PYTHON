import math
import random


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



def fermat(t, n):
    if n == 3:
        return True
    else:
        for i in range(1,t):
            a = random.randint(2,n-2)
            r = solve(a, n - 1, n)
            if r != 1:
                return False
        return True

if __name__ == '__main__':

    n = int(input('Enter n = '))
    t = int(input('Enter t = '))
    if fermat(t, n):
        print('Prime')
    else:
        print('Not Prime')