import sys
sys.stdin = open("in22.txt","rt")

n = int(input())
a = list(map(int,input().split()))
a.sort()
result = 0
tmp = []
second = []
print(a)

for i in a:
    result += i
    tmp.append(result)
for j in tmp:
    result += j
    second.append(result)
print(second)