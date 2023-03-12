import math
from security_algorithm_1 import arrToInt,enterArr

def integer_multiprecision( A, B,p,W): #Bai 6
    t = math.ceil(math.log(p, 2)/W)
    C=[0]*2*t
    A.reverse()
    B.reverse()
    for i in range(t):
        U =0
        V = 0
        for j in range(t):
            
            
            U ,V = convertUV(C[i+j]+A[i]*B[j]+U,W)
            C[i+j]=V
        C[i+t] = U
    return C[::-1]

def convertUV(UV,W):
    binary = "0b"+str(bin(UV))[2:].zfill(2*W)
    U = int(binary[2:W+2],2)
    V = int(binary[W+2:2*W+2],2)
    return U,V

def gcd(a,b): # Bai 7
    if a == 0 or b == 0:
        return "Error"
    else:
        while b != 0:
            t = b
            b = a%b
            a = t
        return a
    

def extendedEuclideanAlgorithm(a, b): # Bai 7
    d = 0
    x = 0
    y = 0
    
    if b == 0:
        d = a
        x = 1
        y = 0
    else:
        x2 = 1
        x1 = 0
        y2 = 0
        y1 = 1
        while b > 0:
            q = int(a/b)
            r = a -q*b
            x = x2 -q*x1
            y = y2 - q*y1
            a =b
            b = r
            x2=x1
            x1=x
            y2 = y1
            y1 = y
        d = a
        x = x2
        y = y2
    
    return [d,x,y]


def inversionInFpUsingTheExtendEuclideanAlgorithm(a,p): #Bai 8
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u != 1:
        q = int(v/u)
        r = v - q*u
        x = x2 - q*x1
        v = u
        u = r
        x2 = x1
        x1 = x
    
    return x1

        
    
if __name__ == "__main__":
    # test
  
    print(inversionInFpUsingTheExtendEuclideanAlgorithm(45682375,489573857))
