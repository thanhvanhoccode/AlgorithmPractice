#https://codelearn.io/training/1792
def isMonotonous(sequence):
    increase = True
    decrease = True
    i =0
    while (increase or decrease) and i < len(sequence)-1:
        if sequence[i] > sequence[i+1]:
            increase = False
        elif sequence[i] < sequence[i+1]:
            decrease = False
        else:
            return False

        i += 1
    return increase or decrease
