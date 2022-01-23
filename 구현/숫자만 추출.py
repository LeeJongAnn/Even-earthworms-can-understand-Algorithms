import sys
sys.stdin = open("in7.txt", "rt")
n = input()
res = 0
cnt = 0
for x in n:
    if x.isdigit():
        res = (res * 10) + int(x)
print(res, end=" ")
for j in range(1, res + 1):
    if res % j == 0:
        cnt += 1
print(cnt)