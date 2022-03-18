import sys
sys.stdin = open("in29.txt", "rt")
n = int(input())
first = []
second = []
for _ in range(n):
    m = int(input())
    for i in range(m):
        a,b = map(int,input().split())
        first.append((a,b))
    print(first)
    first.sort(reverse=True)
    print(first)
    cnt = 0
    for x,y in first:
        largest = 0
        if largest<y:
            largest = y
            cnt += 1
    print(cnt)
# tmp = []
# temp2 = []
# for i in range(m):
#     data = list(map(int, input().split()))
#     tmp.append(data)
# tmp.sort(reverse=True)
# print("첫번째 :",tmp)
#
# k = int(input())
# for j in range(k):
#     data = list(map(int, input().split()))
#     temp2.append(data)
# temp2.sort(reverse=True)
# print("두번째 :", temp2)
#
# largest = 0
# cnt = 0
#
# print(cnt)
#
