#https://codelearn.io/training/2322
def sock_merchant(sizes):
    d = {}
    for size in sizes:
        if d.get(size, 0):
            d[size] += 1
        else:
            d[size] = 1
    count = 0
    for key in d:
        count += d[key]//2
    return count
