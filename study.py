import sys
from collections import deque

sys.stdin = open("first.txt","rt")

n,m = map(int,input().split())
num = list(map(int,input().split()))


Q = [(pos,val) for pos,val in enumerate(num)]
Q = deque(Q)
cnt = 0

while True:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0] == m:
            print(cnt)
            break
