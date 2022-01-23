import sys
sys.stdin = open("in1.txt","rt")
n = int(input())
body = []

for i in range(n):
    length,weight = map(int,input().split())
    body.append((length,weight))

body.sort(reverse=True)
largest = 0
cnt = 0
print(body)
for x,y in body:
    if largest<y:
        largest=y
        cnt += 1
    print(x,y)
print(cnt)
