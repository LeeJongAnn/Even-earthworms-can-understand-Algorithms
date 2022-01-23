import sys
import time
start = time.time()
sys.stdin = open("in22.txt", "rt")
n = int(input())
print(n)
data = list(map(int,input().split()))
print(data)
data.sort()
print(data)
target = 1
for i in data:
    if target<i:
        break
    target += i
print(target)
print("시간:" , start-time.time())

# n = int(input())
# a = list(map(int,input().split()))
# a.sort()
# result = 0
# tmp = []
# second = []
# print(a)
#
# for i in a:
#     result += i
#     tmp.append(result)
# for j in tmp:
#     result += j
#     second.append(result)
# print(second)
