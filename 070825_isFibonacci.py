#https://codelearn.io/training/2361
def isFibonacci(k):
    F0 = 1
    tmp = 0
    Fn = 1
    while Fn < k:
        tmp = Fn
        Fn += F0
        F0 = tmp
    if Fn == k:
        return True
    else: return False
