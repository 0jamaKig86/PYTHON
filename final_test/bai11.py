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
    sum=0
    for i in range(1,n+1):
        if isPrime(i):
            sum+=i
    print("Sum =",sum)