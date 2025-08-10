#https://codelearn.io/training/2359
def countingStar(matrix):
    visited = []
    n = len(matrix)
    m = len(matrix[0])
    count = 0

    for i in range(n):
        visited.append([])
        for j in range(m):
            visited[i].append(0)
    for i in range(n):
        for j in range(m):
            #Ô đánh dấu bỏ qua, ô đen đánh dấu và bỏ qua
            if visited[i][j] == 1:
                continue
            if visited[i][j] == 0 and matrix[i][j] == 1:
                visited[i][j] = 1
                continue
            queue = [(i, j)]
            count += 1
            #Duyệt hết phần tử liên thông
            while queue:
                u, v = queue.pop(0)
                #Ô đánh dấu bỏ qua, ô đen đánh dấu và bỏ qua
                if visited[u][v] == 1:
                    continue
                if visited[u][v] == 0 and matrix[u][v] == 1:
                    visited[u][v] = 1
                    continue
                #Đánh dấu ô hiện tại
                visited[u][v] = 1
                #Thêm ô xung quanh
                if v+1 < m:
                    if visited[u][v+1] == 0:
                        queue.append((u, v+1))
                if v-1 >-1:
                    if visited[u][v-1] == 0:
                        queue.append((u, v-1))
                if u+1 < n:
                    if visited[u+1][v] == 0:
                        queue.append((u+1, v))
                if u-1 > -1:
                    if visited[u-1][v] == 0:
                        queue.append((u-1, v))
    
    return count
