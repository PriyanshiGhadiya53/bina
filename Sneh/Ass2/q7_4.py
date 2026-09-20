from collections import deque
def bfs(graph,start):
    visited=set()
    queue=deque([start])

    while queue:
        node=queue.popleft()

        if node not in visited:
            print(node,end=" ")
            visited.add(node)

        for n in graph[node]:
            if n not in visited:
                queue.append(n)

    return visited
graph={
     'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B', 'E'],
    'E': ['D']
}

print("\nBFS traverse:\n")

visited=bfs(graph,'A')

if(len(visited)==len(graph)):
    print("\ngraph is connected")

else:
    print("\ngraph is notconnected")