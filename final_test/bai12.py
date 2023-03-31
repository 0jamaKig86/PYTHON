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
    # print(prime)
    for i in  (0, len(prime)+1):
        b=sum(prime[i:i+4]) 
        if isPrime(b) and b <= n :

            print(prime[i:i+4], end= ' ')
        elif isPrime(b) and b >= n:
            print("No match!!!")
        