#https://codelearn.io/training/2362
def pagesNumbering(n):
    n = str(n)
    m = len(n)-1
    k = 10
    if int(n) > 9:
        count = ((int(n) + 1)-(k**m))*(m+1)
    else: 
        return int(n)
    while m >= 1:
        count += (k**m - k**(m-1))*(m)
        print(k**m, "-", k**(m-1), "*", m)
        m-=1
    return count
