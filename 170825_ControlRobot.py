https://codelearn.io/training/3194
def control_robot(start,directions):
    huong = ['B', 'DB', 'D', 'DN', 'N', 'TN', 'T', 'TB']
    robot = 0
    for i in range(len(huong)):
        if huong[i] == start:
            robot = i
            break
    for step in directions:
        if step == "T":
            robot-=1
        else:
            robot += 1
    return huong[robot%8]
