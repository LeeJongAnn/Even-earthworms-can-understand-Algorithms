from collections import deque
import sys
import time
start = time.time()
sys.stdin = open("in23.txt", 'rt')
n = int(input())
for i in range(n):
    x, y = input().split()
    text = ''
    for i in y:
        text += int(x) * i
    print(text)

# n = int(input())
# tmp,tmp2 = [],[]
# a,b = input().split()
# for j in range(int(a)):
#     tmp.append(b[j]*int(a))
# result1 = ''.join(tmp)
# print(result1)
# a,b = input().split()
# for k in range(int(a)-1):
#     tmp2.append(b[k]*int(a))
# result2 = ''.join(tmp2)
# print(result2)