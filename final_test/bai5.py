import math

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
        return True


if __name__ == "__main__":

    a = int(input("Enter A = "))
    b = int(input("Enter B = "))
    sum=0
    if a < b:
        for i in range(a, b, 1):
            if isPrime(i):
                sum+=i
        print(sum)

    elif a > b:
        for i in range(b, a, 1):
            if isPrime(i):
                sum+=i
        print(sum)

    else:
        print("A != B !!!")
