#https://codelearn.io/training/3073
def replace_special_char(s):
    ss = ["a", 'o', 'e', 'u', 'i', 'y']
    result = ""
    for i in s:
        if i.isupper():
            for j in ss:
                if i.lower() == j:
                    result += "."
                    break
            else:
                result += i.lower()
        else:
            for j in ss:
                if i == j:
                    result += "."
                    break
            else:
                result += i
    return result
