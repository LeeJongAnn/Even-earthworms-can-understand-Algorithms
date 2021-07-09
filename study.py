import sys
from collections import deque
sys.stdin = open("first.txt","rt")

n,m = map(int,input().split())

num = list(map(int , str(n)))

dq = deque(num)

while True:
    for x in dq:
        cur = dq.popleft()
        dq.append(cur)
