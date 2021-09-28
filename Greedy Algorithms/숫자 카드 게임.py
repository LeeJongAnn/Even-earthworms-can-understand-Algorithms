import sys
sys.stdin = open("in17.txt", "rt")

s,e = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
# c = list(map(int,input().split()))
a.sort(reverse=True)
first = a[-1]
b.sort(reverse=True)
second = b[-1]
# c.sort(reverse=True)
# third = c[-1]
tmp = 0
for i in range(s):
    if first>tmp:
        tmp = first
    elif second>tmp:
        tmp = second
    # elif third>tmp:
    #     tmp = third
print(tmp)

