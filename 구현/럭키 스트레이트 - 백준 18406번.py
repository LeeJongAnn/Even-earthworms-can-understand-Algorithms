import sys
import time
start = time.time()
sys.stdin = open("11.txt",'rt')
n = input()
print(len(n))
tmp = []
left = 0
right = 0
cnt = 0
for i in range((len(n)//2)):
    left += int(n[i])
for i in range((len(n)//2),len(n)):
    right += int(n[i])
print(left)
print(right)
if left == right:
    print("LUCKY")
else:
    print("READY")
print("시간" , time.time()-start)