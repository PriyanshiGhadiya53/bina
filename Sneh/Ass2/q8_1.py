def dfs(matrix,start,visited=None):
    if visited is None:
        visited=set()

    print(start,end=" ")
    visited.add(start)

    for n in range(len(matrix)):
        if matrix[start][n]==1 and n not in visited:
            dfs(matrix,n,visited)
matrix=[ [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0]]
print("\nDFS traverse\n")
dfs(matrix,0)