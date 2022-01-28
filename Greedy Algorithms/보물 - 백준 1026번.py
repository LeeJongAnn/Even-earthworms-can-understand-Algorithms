import sys
sys.stdin = open("in24.txt","rt")
n = int(input())
print(n)
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(a)
print(b)
a.sort()
print(a)
result = 0
for i in range(n):
     result += min(a)*max(b)
     a.pop(0)
     b.pop(b.index(max(b)))
print(result)