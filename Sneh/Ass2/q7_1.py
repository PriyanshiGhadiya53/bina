from collections import deque
def bfs(matrix,start):
    visited=set()
    queue=deque([start])

    while queue:
        node=queue.popleft()
        if(node not in visited):
            print(node,end=" ")
            visited.add(node)

        for n in range(len(matrix)):
            if(matrix[node][n]==1 and n not in visited):
                queue.append(n)

matrix=[
    [0,1,1,1,0],
    [1,0,0,0,0],
    [1,0,1,0,1],
    [0,1,1,0,1],
    [0,0,1,0,1]
]
print("BFS travers")
bfs(matrix,0)