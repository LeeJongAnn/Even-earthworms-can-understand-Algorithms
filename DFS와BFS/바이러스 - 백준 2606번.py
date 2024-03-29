import sys
from collections import deque
sys.stdin = open("in11.txt", 'rt')
n = int(input())
m = int(input())
graph = [[] * n for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

cnt = 0
visited = [0] * (n+1)

def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1
dfs(1)
print(cnt)