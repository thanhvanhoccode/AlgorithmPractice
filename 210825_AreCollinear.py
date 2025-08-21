#https://codelearn.io/training/2344
def collinear(coordinates):
    AB = [coordinates[1][0]-coordinates[0][0], coordinates[1][1]-coordinates[0][1]]
    AC = [coordinates[2][0]-coordinates[0][0], coordinates[2][1]-coordinates[0][1]]
    S_ABC = abs(AB[0]*AC[1] - AB[1]*AC[0])/2
    return S_ABC == 0
