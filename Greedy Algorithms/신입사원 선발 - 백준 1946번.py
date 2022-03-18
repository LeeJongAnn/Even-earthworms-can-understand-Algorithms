import sys
sys.stdin = open("in29.txt", "rt")
T = int(input())

for i in range(0, T):
    Cnt = 1
    people = []

    N = int(input())
    for i in range(N):
        Paper, Interview = map(int, sys.stdin.readline().split())
        people.append([Paper, Interview])

    people.sort()
    Max = people[0][1]

    for i in range(1, N):
        if Max < people[i][1]:
            Cnt += 1
            Max = people[i][1]
    print(Cnt)



# n = int(input())
# first = []
# second = []
# for _ in range(n):
#     m = int(input())
#     for i in range(m):
#         a,b = map(int,input().split())
#         first.append((a,b))
#     print(first)
#     first.sort(reverse=True)
#     print(first)
#     cnt = 0
#     largest = 0
#     for x,y in first:
#         if largest<y:
#             largest = y
#             cnt += 1
#     print(cnt)

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
