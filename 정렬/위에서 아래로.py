import sys
sys.stdin = open("in1.txt","rt")

n = int(input())
tmp = []
for i in range(n):
    num = int(input())
    tmp.append(num)
tmp.sort(reverse=True)

for i in tmp:
    print(i,end=" ")