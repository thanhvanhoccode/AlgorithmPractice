#https://codelearn.io/training/3193
#Thật ra quên cách sắp xếp ngược nên sắp tăng dần rồi duyệt từ cuối :)
def removeSubStrings(s):
    chose = []
    s1 = 0
    for i in s:
        if i == "1":
            s1+=1
        else:
            chose.append(s1)
            s1 = 0
    if s1 != 0:
        chose.append(s1)
    chose.sort()
    A = 0
    B = 0
    for i in range(len(chose)-1, -1, -2):
        A += chose[i]
    for i in range(len(chose)-2, -1, -2):
        B += chose[i]
    if A > B:
        return [1, A]
    return [2, B]
