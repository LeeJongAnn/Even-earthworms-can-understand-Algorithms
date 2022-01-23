import sys
sys.stdin = open("in10.txt",'rt')

n = int(input())

distance = list(map(int,input().split()))
oil = list(map(int,input().split()))
firstoil = oil[0]
result = 0
for i in range(len(distance)):
    if firstoil>=oil[i]:
        firstoil = oil[i]
        result += distance[i] * firstoil
    if firstoil<oil[i]:
        result += distance[i] * firstoil
print(result)