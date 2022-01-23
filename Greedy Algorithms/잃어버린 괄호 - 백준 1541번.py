import sys
sys.stdin = open("in8.txt",'rt')
a = input().split('-')
tmp = []
print(a)
result = 0
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    tmp.append(cnt)
n = tmp[0]

for i in range(1,len(tmp)):
    n -= tmp[i]
print(n)
