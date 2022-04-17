import sys
from collections import deque
sys.stdin = open("in19.txt", "rt")

n,k = map(int,input().split())
max_result = -1e9

def dfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break

        for j in (x-1,x+1,x*2):
            if 0<=j <=MAX and not dist[j]:
                dist[j] = dist[x] + 1
                q.append(j)


MAX = 100000
dist = [0] * MAX

dfs()