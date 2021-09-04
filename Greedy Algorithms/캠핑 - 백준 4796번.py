import sys
sys.stdin = open("in15.txt", "rt")


tmp = []
for i in range(3):
    first = list(map(int ,input().split()))
    tmp.append(first)
for j in tmp:
