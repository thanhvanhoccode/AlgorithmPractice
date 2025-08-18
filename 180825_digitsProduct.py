#https://codelearn.io/training/1794
def digitsProduct(product):
    if product == 0:
        return 10
    if product == 1:
        return 1
    d = ""
    i = 9
    while i > 1:
        if product%i == 0:
            d = str(i) + d
            product = product//i
        else:
            i -= 1
    if product > 1:
        return -1
    return int(d)
