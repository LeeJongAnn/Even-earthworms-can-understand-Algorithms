import sys
sys.stdin = open("in17.txt", "rt")
s,e = map(int,input().split())
low1 = list(map(int,input().split()))
low2 = list(map(int,input().split()))
print(low1)
print(low2)
low1.sort(reverse=True)
low2.sort(reverse=True)
print(low1)
print(low2)
first = low1[-1]
second = low2[-1]
tmp = 0
print(first)
print(second)
for i in range(1):
    if first>tmp:
        tmp = first
    if second>tmp:
        tmp = second
print(tmp)