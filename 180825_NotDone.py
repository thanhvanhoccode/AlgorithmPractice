#https://codelearn.io/training/1794
def digitsProduct(product):
    if product == 0:
        return 10
    if product == 1:
        return 1
    dct = {}
    i = 2
    while i <= 9:
        if product % i == 0:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
            product = product//i
        else:
            i += 1
    if dct == {}:
        return -1
    if product > 1:
        if product in dct:
            dct[product] += 1
        else:
            dct[product] = 1
    print(dct)
    if dct.get(3, 0) != 0:
        if dct[3] > 1:
            dct[9] = dct[3]//2
            dct[3] = dct[3]%2
        if dct.get(2, 0) != 0 and dct.get(3, 0) != 0:
            dct[2] -= 1
            dct[3] -= 1
            dct[6] = 1
        if dct[2] >1:
            dct[4] = dct[2] //2
            dct[2] = dct[2] % 2
        
    print(dct)
    product = ""
    for i in range(2, 10):
        if dct.get(i, 0) != 0:
            product += str(i)*dct[i]
    return int(product)
