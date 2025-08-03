#https://codelearn.io/training/1790
import math
def thuaso(n):
    thua_so = []
    for i in range(2, int(math.sqrt(n))+1):
        while n %i == 0:
            thua_so.append(i)
            n = n//i
    if thua_so == []:
        return [n]
    elif n != 1:
        return thua_so + [n]
    else:
        return thua_so

def lastDigitDiffZero(n):
    dic = {1:0}
    s = 1
    for i in range(1, n + 1):
        li = thuaso(i)
        #add vào
        for k in li:
            if dic.get(k) == None:
                dic[k] = 1
            else:
                dic[k] += 1
    print(dic)
    if (dic.get(2) != None and dic.get(5) != None):
        minMu = min(dic.get(2), dic.get(5))
        dic[2] -= minMu
        dic[5] -= minMu
    for key in dic:
        s *= key**dic[key]
    return int(str(s)[-1])
