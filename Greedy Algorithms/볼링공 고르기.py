import sys
import time
start = time.time()
sys.stdin = open("in23.txt", "rt")
n, m = map(int, input().split())
print(n, m)
num = list(map(int, input().split()))
print(num)
array = [0] * 11
for i in num:
    array[i] += 1
print(array)
result = 0
for i in range(1, m + 1):
    n -= array[i]
    print("n의 값은:", n)
    result += array[i] * n
    print("result", i, "의 값은:", result)
print(result)
print("시간:", time.time() - start)
