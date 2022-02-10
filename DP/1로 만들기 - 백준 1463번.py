import sys
sys.stdin = open("first.txt", 'rt')
n = int(input())
result = 0
cnt = 0
while n>=1:
    if n%3!=0:
        n -= 1
        cnt+= 1
    n//=3
    cnt +=1
print(cnt)
