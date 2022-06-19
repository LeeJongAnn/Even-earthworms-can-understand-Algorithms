import time
start = time.time()
from math import sqrt
def solution(n):
    num = set(range(2, n+1))
    for i in range(2, int(sqrt(n+1))+1):
        if i in num:
            num -= set(range(2*i, n+1,i))
    return len(num)
print(solution(10))
end = time.time()
print(end-start)