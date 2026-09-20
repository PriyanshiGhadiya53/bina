from collections import deque
def bfs(graph,start):
    visited=set()
    queue=deque([start])

    while queue:
        node=queue.popleft()
        if(node not in visited):
            print(node,end=" ")
            visited.add(node)

        for n in graph[node]:
            if(n not in visited):
                queue.append(n)    


graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B'],
    'F':['C']
}
print("BFS travers:")
bfs(graph,'A')