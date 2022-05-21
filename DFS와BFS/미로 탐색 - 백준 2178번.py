import sys
from collections import deque
sys.stdin = open("in17.txt","rt")
n,k = map(int,input().split())

graph = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for _ in range(n):
    graph.append(list(map(int,input().strip())))

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0>nx or 0>ny or nx>=n or ny>=k:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
    return

bfs(0,0)
for z in graph:
    print(z)

print(graph[n-1][k-1])



