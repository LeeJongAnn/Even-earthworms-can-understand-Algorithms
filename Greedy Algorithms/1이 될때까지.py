import sys
import time
start = time.time()
sys.stdin = open("in18.txt", "rt")
n,k = map(int,input().split())
print(n,k)
cnt = 0
while n>=k:
    while n%k!=0:
        n -= 1
        cnt +=1
    n//=k
    cnt+=1
while n>1:
    n -= 1
    cnt +=1
print(cnt)
print("시간: " , start - time.time())