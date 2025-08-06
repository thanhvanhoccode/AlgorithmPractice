#https://codelearn.io/training/2354
def colorfulFlowers(arr):
    k = 1
    result = 0
    arr.append(-1)
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            k += 1
        elif result < k:
            result = k
            k = 1
        else:
            k = 1
    return result
