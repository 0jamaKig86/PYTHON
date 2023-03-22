import math


def SieveOfEratosthenes(num):  # Bai 9
    prime = [True for i in range(num+1)]
# boolean array
    p = 2
    while (p * p <= num):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers

    for p in range(2, num+1):
        if prime[p]:
            print(p)
            
def pollardsRho(n):  # Bai 10
    a = b = 2
    for i in range(100):
        a = (a*a + 1) % n
        b = (b*b + 1) % n
        b = (b*b + 1) % n
        d = gcd(a-b, n)
        if 1 < d < n:
            return d


def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


def primeFactors(n):
    prime = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        prime.append(2)

        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n))+1, 2):

        # while i divides n , print i and divide n
        while n % i == 0:
            prime.append(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        prime.append(int(n))

    unique_Prime = list(dict.fromkeys(prime))
    numberOfUniquePrime = []
    # print(unique_Prime)
    for i in unique_Prime:
        numberOfUniquePrime.append(prime.count(i))
    print(unique_Prime, numberOfUniquePrime)


if __name__ == "__main__":

    primeFactors(203415121)
    # print(pollardsRho(717469))
    # # print(SieveOfEratosthenes(1000))
    
