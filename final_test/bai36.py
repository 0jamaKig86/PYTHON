
def last_occurrence(T, P): 
    L = {}
    for i in range(len(P)):
        if P[i] not in L:
            for j in range(len(P)):
                if P[i] == P[j]:
                    value = j
            L[P[i]] = value
    for i in range(len(T)):
        if T[i] not in L:
            L[T[i]] = -1
    return L


def boyerMoore(T, P):
    L = last_occurrence(T, P)
    j = len(P) - 1
    i = len(P) - 1
    while True:
        if i >= len(T):
            return -1
        while T[i] == P[j]:
            i -= 1
            j -= 1
            if j + 1 == 0:
                return i + 2
        i = i + len(P) - min(j, 1 + L[T[i]])
        j = len(P) - 1

if __name__ == "__main__":

    T = input('Enter string T = ')
    P = input('Enter string P = ')
    index = boyerMoore(T, P)
    if index != -1:
        print(f'P in T at  : {index}')
    else:
        print('P no exist!!!')