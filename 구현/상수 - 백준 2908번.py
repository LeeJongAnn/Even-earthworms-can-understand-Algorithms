from collections import deque
import sys
import time
start = time.time()
sys.stdin = open("first.txt", 'rt')
n,k = input().split()
tmp = []
data = []
for i in range(len(n)):
    tmp.append(n[i])
    data.append(k[i])
result = 0
tmp = list(reversed(tmp))
data = list(reversed(data))
result1 = ''.join(tmp)
result2 = ''.join(data)
last = max(result1,result2)
print(last)
# for i in range(len(tmp)):
#     result = tmp.pop()
#     data.append(result)
# for x in data:
#     print(x,end="")
#
end = time.time()
print()
print("걸린 시간:" ,start-end)