import math


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True

def searchXY(prime ,S):
    XY=[]
    for k in prime:
        for i in S:
                for j in S:
                    if i<j:
                        if isPrime(i + j) and i+j == k:
                            XY.append([int(math.sqrt(i)),int(math.sqrt(j))])
    if len(XY) == 0:
        return False
    else:
        return XY


if __name__ == '__main__':
    A=int(input("Enter A = "))
    B=int(input("Enter B = "))
    S=[]
    for i in range(1,int(math.sqrt(B))+1,1):
        S.append(i*i)

    prime=[]
    for i in range(A,B):
        if isPrime(i):
            prime.append(i)
    if len(prime) == 0:
        print("Not exist!!!")

    else:
        if searchXY(prime,S)==False:
            print("X,Y not exist!!!")
        else:
            print("[X, Y] : ",searchXY(prime,S))



