import sys
import time
start = time.time()
sys.stdin = open("in20.txt", "rt")
data = input()
print(data)
first = int(data[0])
print(first)
result = 0
for i in range(1,len(data)):
    num = int(data[i])
    if num<=1 or first<=1:
        first += num
    else:
        first *= num
print(first)

print("time :", time.time() - start)