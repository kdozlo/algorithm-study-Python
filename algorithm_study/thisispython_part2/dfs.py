#재귀함수로 dfs 구현
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#반복문으로 dfs 구현
def dfs_2(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    s=[1]
    while s:
        chk = 0
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                s.append(v)
                v = i
                s.append(v)
                print(v, end=' ')
                chk = 1
                break
        if not chk:
            v = s.pop()
            

       

    

graph = [[],
        [2,4],
        [5,8],
        [],
        [6, 7],
        [],
        [],
        [],
        [3]
        ]

visited = [False]*9
dfs(graph, 1, visited)
print()
visited_2 = [False]*9
dfs_2(graph, 1, visited_2)