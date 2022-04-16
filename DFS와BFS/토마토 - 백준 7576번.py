from collections import deque
import sys
sys.stdin = open("in18.txt",'rt')

n,k = map(int,input().split())

graph = []

for _ in range(k):
    graph.append(list(map(int,input().split())))

for z in graph:
    print(z)

dx = [0,1,0,-1]
dy = [1,0,-1,0]
q = deque()
def bfs(x,y):
    global count
    count = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<k:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[y][x] + 1
                q.append((nx,ny))
                count += 1
    return
for i in range(n):
    for j in range(k):
        if graph[i][j] == 1:
            q.append((i,j))
print(count)