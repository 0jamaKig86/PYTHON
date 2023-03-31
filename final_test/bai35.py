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




def miller_rabin(n, t):
    if n == 2 or n == 3:
        return True

    elif n == 1:
        return False
    else:
        r = n - 1
        s = 0
        while r % 2 == 0:
            s += 1
            r /= 2

            for i in range(1, t):
                a = random.randint(2, n-2)
                y = solve(a, int(r), n)
                if y != 1 and y != n - 1:
                    j = 1
                    while j <= s - 1 and y != n - 1:
                        y = (y * y) % n
                        if y == 1:
                            return False
                        j += 1
                    if y != n - 1:
                        return False

if __name__ == "__main__":

    n = int(input('Enter n = '))
    t = int(input('Enter t = '))
    if miller_rabin(n, t):
        print('Prime')
    else:
        print('Not prime!!!')