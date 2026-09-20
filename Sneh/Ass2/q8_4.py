def dfs(graph,start,visited=None):
    if visited is None:
        visited = set()

    print(start,end=" ")
    visited.add(start)

    for n in graph[start]:
        if n not in visited:
            dfs(graph,n,visited)

    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B', 'E'],
    'E': ['D']
}
print("DFS traverse")
visited=dfs(graph,'A')
if(len(visited)==len(graph)):
    print("Graph is connected.")
else:
    print("Graph is not connected.")
