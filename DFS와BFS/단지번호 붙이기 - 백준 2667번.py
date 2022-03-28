import sys
from collections import deque
sys.stdin = open("in12.txt","rt")

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x,y,graph):
    q = deque()
    q.append((x,y))
    graph[x][y] = value
    count[value] = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == value or graph[nx][ny] == 0:
                continue
            graph[nx][ny] = value
            count[value] += 1
            q.append((nx,ny))
    return
n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().strip())))

count = {}
value = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j,graph)
            value += 1

ary = sorted(list(count.values()))
print(len(ary))
for i in ary:
    print(i)