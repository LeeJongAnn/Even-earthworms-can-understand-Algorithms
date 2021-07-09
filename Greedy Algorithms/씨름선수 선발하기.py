import sys
sys.stdin = open("in1.txt","rt")
n =int(input())
body = []

for i in range(n):
    s,e = map(int , input().split())
    body.append((s,e))

body.sort(reverse=True)
largest = 0
cnt = 0

for x ,y in body:
    if y>largest:
        largest=y
        cnt+=1
print(cnt)