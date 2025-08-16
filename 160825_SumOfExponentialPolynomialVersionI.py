#https://codelearn.io/training/3228
def soep(n,k):
    s = 0
    for i in range(1, n+1):
        s += i**k
    return s%(10**9 + 7)
