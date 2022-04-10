import sys
from collections import deque
sys.stdin = open("in17.txt","rt")

n,k = map(int,input().split())

graph = []


dx = [0,1,0,-1]
dy = [1,0,-1,0]


for _ in range(n):
    graph.append(list(map(int,input().strip())))

for q in graph:
    print(q)

count = 1
def bfs(x,y,graph):
    q = deque()
    q.append((x,y))
    graph[x][y] = value

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<k and graph[nx][ny] == 1:
                graph[nx][ny] = value
    return

value = 1
for i in range(n):
    for j in range(k):
        if graph[i][j] == 1:
            bfs(i,j,graph)
            count += 1

print(count)


