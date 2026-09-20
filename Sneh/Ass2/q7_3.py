from collections import deque
def bfs(graph,start,target):
    visited=set()
    queue=deque([[start]])

    while queue:
        path=queue.popleft()
        node=path[-1]

        if target==node:
            return path

        if(node not in visited):
            print(node,end=" ")
            visited.add(node)


            for n in graph[node]:
                if n not in visited:
                    newpath=path + [n]
                    queue.append(newpath)
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start='A'
target='F'

path=bfs(graph,start,target)
print("shorted path:-> ",path)