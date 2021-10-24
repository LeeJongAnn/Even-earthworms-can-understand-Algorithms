import sys
sys.stdin = open("11.txt",'rt')
n = int(input())
tmp = []
left = 0
right = 0
for i in str(n):
    tmp.append(i)
    left += tmp[i]
print(left)