from collections import deque
import sys
sys.stdin = open("in2.txt", 'rt')
temp = []
n = input()
k = input()
print(n)
print(k)
print(k.find(n[0]))
cnt = 0
for i in range(len(n)):
    result=k.find(n[i])
    temp.append(result)
    if temp[i] == -1:
        cnt -=1
    else:
        cnt += 1
print(temp)
print(cnt)

