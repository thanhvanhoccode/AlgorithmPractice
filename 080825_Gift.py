#https://codelearn.io/training/3221
def gift(n,k):
    arr = [0 for i in range(n)]
    for K in k:
        u = K[0]-1
        v = K[1]
        t = K[2]
        arr[u] += t
        if v == n:
            continue
        arr[v] -= t
    for i in range(1, n):
        arr[i] += arr[i-1]
    return arr
