import sys
sys.stdin = open('in12.txt','rt')
N = int(input())
rope = [int(sys.stdin.readline()) for i in range(N)]
rope.sort()
result=0
for i in range(len(rope)):
    if result < N * rope[i]:
        result = N * rope[i]
        N -= 1
    else:
        N -= 1
print(result)

# n = int(input())
# a = int(input())
# b = int(input())
# result = 0
#
# for i in range(n):
#     if a<b:
#         result += a
#     else:
#         result += b
# print(result)