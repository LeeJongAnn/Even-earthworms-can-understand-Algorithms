import sys
import time
start = time.time()
sys.stdin = open("in28.txt", "rt")
n = input()
tmp = 0
List = []
for i in range(len(n)):
    tmp = n[i]
    List.append(tmp)
List.sort(reverse=True)
temp = int(''.join(List))
if temp%30 != 0:
    print(-1)
else:
    print(temp)
print("시간: " ,  time.time() - start)