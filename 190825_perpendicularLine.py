#https://codelearn.io/training/2212
def perpendicular_line(arr):
    vAB = [arr[1][0]-arr[0][0], arr[1][1]-arr[0][1]]
    vCD = [arr[3][0]-arr[2][0], arr[3][1]-arr[2][1]]
    if vAB == [0, 0] or vCD == [0, 0]:
        return False
    return not (vAB[0]*vCD[0] + vAB[1]*vCD[1])
