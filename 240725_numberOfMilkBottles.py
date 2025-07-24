#https://codelearn.io/training/1793?tab=description&activityId=0&activityType=12&token=
def numberOfMilkBottles(a,b,c):
    n = 0
    while c >= a:
        n += c//a
        c = (c//a)*b + c%a
    return n