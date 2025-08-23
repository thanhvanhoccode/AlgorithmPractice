#https://codelearn.io/training/3226
def fibSum(n):
    MOD = 10**9 + 7
    sumF = 0
    F_2, F_1 = 0, 1
    for _ in range(n):
        sumF = (sumF + F_1) % MOD
        F_2, F_1 = F_1, (F_2 + F_1) % MOD
    return sumF
