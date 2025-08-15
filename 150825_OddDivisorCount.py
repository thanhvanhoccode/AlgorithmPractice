#https://codelearn.io/training/3236
def solve(a,b):
    count = 0
    for i in range(a, b+1):
        if math.sqrt(i) == int(math.sqrt(i)):
            count+= 1
    return count
