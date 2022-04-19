from collections import deque
import sys
sys.stdin = open("in18.txt",'rt')

n,k = map(int,input().split())

graph = []

for _ in range(k):
    graph.append(list(map(int,input().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0>nx or 0>ny or nx>=k or ny>=n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
    return

for i in range(k):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)
res = 0
for z in graph:
    for w in z:
        if w == 0:
            print(-1)
            exit(0)
    res = max(res,max(z))
print(res-1)