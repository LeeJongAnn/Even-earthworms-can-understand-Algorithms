import sys
sys.stdin = open("in24.txt","rt")
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(n)
print(a)
print(b)
a.sort()
print(a)
result = 0
for x in b:
    for i in range(n):
        result += a[i]*x
        print(a[i],x)
        print(result)



