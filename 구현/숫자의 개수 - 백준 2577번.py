import sys
sys.stdin = open("in18.txt", "rt")

a = int(input())
b = int(input())
c = int(input())

result = str(a*b*c)
array = [0] * 10
tmp = []
for x in result:
    tmp.append(x)
    array[int(x)] += 1

for i in range(10):
    print(array[i])