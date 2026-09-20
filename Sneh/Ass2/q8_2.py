def dfs(graph,start,visited=None):
    if visited is None:
        visited = set()

    print(start,end=" ")
    visited.add(start)

    for n in graph[start]:
        if n not in visited:
            dfs(graph,n,visited)

graph = {
'A': ['B', 'C'],
'B': ['A', 'D', 'E'],
'C': ['A'],
'D': ['B'],
'E': ['B']
}
print("DFS traverse: ->\n")
dfs(graph,'A')