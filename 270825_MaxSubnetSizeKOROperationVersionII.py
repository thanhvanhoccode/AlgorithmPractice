#https://codelearn.io/training/3231
def ORnumber(a, b):
    a = cut(bin(a))
    b = cut(bin(b))

    if len(a) > len(b):
        b = "0"*(len(a)-len(b)) + b
    elif len(a) < len(b):
        a = "0"*(len(b)-len(a)) + a

    result = ""
    for i in range(len(a)):
        result += str(int(a[i]) or int(b[i]))

    return int(result, 2)
def cut(s):
    for i in range(2, len(s)):
        if s[i] !=  "0":
            return s[i:]
    return "0"
def solve(n,k,a):
    if k == 1:
        return max(a)
    result = a[0]
    for i in range(1, len(a)):
        result = ORnumber(result, a[i])

    return result
