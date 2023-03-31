import math
prime = []
test=[]
def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True

def solve(M,sum,I,count):

    for i in range(I,len(prime)):
        sum = sum - prime[i]
        test[i] = 1
        count+=1
        if count < M and sum > 0:
            solve(M,sum,i+1,count)
        elif count == M and sum == 0:
            print("[",end=" ")
            for j in range(len(prime)):
                if test[j] == 1:
                    print(prime[j],end=" ")
            print("]")
        sum = sum + prime[i]
        count-=1
        test[i] =0
                    
if __name__ == '__main__':
    M = int(input("Enter M = "))
    N = int(input("Enter N = "))
    
    for i in range(N):
        if isPrime(i):
            prime.append(i)
    test=[0]*len(prime)
    solve(M,N,0,0)