
#                 return False
#         return True
# if __name__ == '__main__':
#     A = enterArr()
#     for i in A:
#         for j in A:
#             if i < j:
#                 if isPrime(math.gcd(i,j)):
#                     print([i,j],end=", ")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0: