import math
def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True

if __name__ == "__main__":
    n = int(input("Enter N = "))
    count=0
    for i in range(2,n+1):
        if isPrime(i):
            print(i,end=" ")
            count+=1
    
    print(count)