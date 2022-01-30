import sys
sys.stdin = open("in29.txt", "rt")
n = input()
m = int(input())
tmp = []
temp2 = []
for i in range(m):
    data = list(map(int, input().split()))
    tmp.append(data)
tmp.sort(reverse=True)
print("첫번째 :",tmp)

k = int(input())
for j in range(k):
    data = list(map(int, input().split()))
    temp2.append(data)
temp2.sort(reverse=True)
print("두번째 :", temp2)

largest = 0
cnt = 0
for x, y in tmp:

print(cnt)

