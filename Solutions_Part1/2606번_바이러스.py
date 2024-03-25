n=int(input())
graph=[[]]; visited=[0]; stack=[]
for _ in range(n):
    graph.append([])
for _ in range(int(input())):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for _ in range(n):
    visited.append('F')

def dfs (node):
    while graph[node]!=[]:
        if visited[graph[node][0]]=='F':
            v=graph[node].pop(0)
            stack.append(v); visited[v]='T'
            return dfs(v)
        elif visited[graph[node][0]]=='T' :
            stack.append(graph[node].pop(0))

    if graph[node]==[] and stack!=[]:
        new_node=stack.pop(len(stack)-1)
        return dfs(new_node)
    #if stack==[]: return
    
visited[1]='T'
stack.append(1)
dfs(1)
    
print(visited.count('T')-1)
