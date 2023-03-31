import math


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True

def searchX(A, B, C,m,l):
    x=[]
    for i in range(m, l,1):
        expr = A * i * i + B * i + C
        if isPrime(expr):
            x.append(i)
    if len(x) !=0:
        return x
    else: 
        return None
    
    


if __name__ == '__main__':
    A = int(input("Enter A = "))
    B = int(input("Enter B = "))
    C = int(input("Enter C = "))
    m = int(input("Enter m = "))
    l = int(input("Enter l = "))

    
    result = searchX(A,B,C,m,l)
    if result != None :
        print("X = ",searchX(A,B,C,m,l))
    else:
        print("X not exist!!!")

