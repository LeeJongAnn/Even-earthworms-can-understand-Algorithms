import sys
sys.stdin = open("in14.txt", "rt")

n = int(input())
tmp = []
results = 0

for i in range(n):
    count = int(input())
    tmp.append(count)
tmp.sort()
print(tmp)
for i in len(tmp):
    for j in tmp:
        results += tmp
