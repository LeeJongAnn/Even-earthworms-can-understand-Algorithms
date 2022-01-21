import sys
import time
start = time.time()  # 시작 시간 저장
sys.stdin = open("in19.txt", "rt")
n = int(input())
data = list(map(int,input().split()))
data.sort()
count = 0
result = 0
for i in data:
    print("i 의 값은" + str(i))
    count += 1
    print("count의 값은" + str(count))
    if count >= i:
        result += 1
        count = 0
    print("result의 값은" + str(result))
print(result)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
