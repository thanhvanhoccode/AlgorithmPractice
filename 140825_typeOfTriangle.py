#https://codelearn.io/training/1814
def typeOfTriangle(a,b,c):
    tmp = [a, b, c]
    tmp.sort()
    if tmp[0] + tmp[1] <= tmp[2] or tmp[0] <= 0:
        return -1
    elif tmp[0]**2 + tmp[1]**2 == tmp[2]**2:
        return 3
    elif tmp[0] == tmp[1] == tmp[2]:
        return 1
    elif tmp[0] == tmp[1] or tmp[1] == tmp[2]:
        return 2
    else:
        return 0

#Cay quá mà, logic đúng hết mà thứ tự kiểm tra sai thế là vẫn không qua test ẩn, kiểm lại khùng luôn
