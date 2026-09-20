def dfs(graph,start,visited=None,parent=None):
    if visited is None:
        visited=set()

    print(start,end=" ")
    visited.add(start)

    for n in graph[start]:
        if n not in visited:
            if dfs(graph,n,visited,start):
                return True
        elif n!=parent:
            return True

    return False

graph={
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}
print("DFS traverse:")

if(dfs(graph,'A')):
    print("\nGraph contains cycle.")
else:
    print("\nGraph not contains cycle.")