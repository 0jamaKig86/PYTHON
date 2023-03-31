import math
def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True

if __name__ == '__main__':
    n=int(input("Enter N = "))
    prime=[]        
    for i in range (1,n+1):
        if isPrime(i):
            prime.append(i)
    
    for i in prime:
        for j in prime:
            if i < j:
                add = i+j
                subtract = abs(i-j)
                if isPrime(add) and isPrime(subtract):
                    print([i,j],end=", ")