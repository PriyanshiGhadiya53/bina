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
    'Ahmedabad': ['Rajkot', 'Vadodara'],
    'Rajkot': ['Ahmedabad', 'Jamnagar'],
    'Vadodara': ['Ahmedabad', 'Surat'],
    'Jamnagar': ['Rajkot'],
    'Surat': ['Vadodara', 'Mumbai'],
    'Mumbai': ['Surat']
}
start='Ahmedabad'
target='Jamnagar'
path=bfs(graph,start,target)
print("\n shorted path:-> ",path)