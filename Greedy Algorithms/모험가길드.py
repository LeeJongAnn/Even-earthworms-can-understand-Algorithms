import sys
sys.stdin = open("in19.txt","rt")

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)

# n = int(input())
# num = list(map(int,input().split()))
# num.sort(reverse=True)
# print(num)
#
# first = num[0]
# cnt = 0
#
# for i in range(1,first):
#     if len(num) == 0:
#         break
#     elif first>num[i]:
#         num.pop()
#         cnt+=1
# print(cnt)
#
