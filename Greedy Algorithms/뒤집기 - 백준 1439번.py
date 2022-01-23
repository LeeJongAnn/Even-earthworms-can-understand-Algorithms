import sys
import time
start = time.time()  # 시작 시간 저장
sys.stdin = open('in21.txt', 'rt')
data = input()
print(data)
change0 = 0
change1 = 0
if data[0] == '0':
    change1 += 1
else:
    change0 += 1
result = 0
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1]=='1':
            change0 += 1
        else:
            change1 += 1
print(min(change0,change1))
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
