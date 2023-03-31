
def failure(P):
    F = {}
    F[0] = -1
    F[1] = 0
    for i in range(2, len(P)):
        prefix = []
        suffix = []  
        j = 1
        a = 1
        k = i
        while j <= i:
            prefix.append(P[0:j])
            suffix.append(P[a:k])
            j += 1
            a += 1
        suffix.reverse()
        suffix.remove('')
        value = 0
        for m in prefix:
            for n in suffix:
                if m == n:
                    if len(m) > value:
                        value = len(m)
        F[i] = value
    return F
 
def kmp(T, P):
    F = failure(P)
    i = 0
    j = 0
    while True:
        if j + i >= len(T):
            return -1
        while P[j] == T[i]:
            i += 1
            j += 1
            if j == len(P):
                return i - len(P) + 1
        i = i + j - F[j]
        if (F[j] == -1):
            j = 0
        else:
            j = F[j]

if __name__ == "__main__":

    T = input('Enter string T = ')
    P = input('Enter string P = ')
    index = kmp(T, P)
    if index != -1:
        print(f'P in T at : {index}')
    else:
        print('P not exist in T')