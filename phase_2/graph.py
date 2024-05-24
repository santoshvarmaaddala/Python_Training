# 1. Constructing adjacency matrix 
n, m = map(int, input().split())
# n is no.of nodes 
# m is no.of edges 
adj = [] 
for i in range(n + 1):
    eachRow = [0] * (n + 1)
    adj.append(eachRow)
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u][v] = 1
    adj[v][u] = 1
 
print(adj)
 
# Output
 
# [[0, 0, 0, 0, 0, 0], 
# [0, 0, 1, 1, 0, 0], 
# [0, 1, 0, 1, 1, 0], 
# [0, 1, 1, 0, 1, 0], 
# [0, 0, 1, 1, 0, 0], 
# [0, 0, 0, 0, 0, 0]]
 
 
# 2. Constructing Adjacency List 
n, m = map(int, input().split())
# n is no.of nodes 
# m is no.of edges 
adj = [] 
for i in range(n + 1):
    adj.append([])
 
[[], [], [], [], []]
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
 
print(adj)
 
 
 
#Output:
#[[], [2, 3], [1, 3, 4], [2, 1, 4], [2, 3], []]
 