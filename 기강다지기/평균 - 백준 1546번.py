import sys
sys.stdin = open("in11.txt", 'rt')

n = int(input())
count = list(map(int,input().split()))
result = 0
count.sort(reverse=True)
first = count[0]
last = count[-1]
final = 0
for i in range(n):
    result = count[i]/first*100
    final += result
report = final/n
print(report)