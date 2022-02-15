import sys
sys.stdin = open("in19.txt", 'rt')

tmp = []
for i in range(1,9):
    n = int(input())
    tmp.append(n)
print(tmp)

index_result = tmp.index(max(tmp))+1
result = max(tmp)
print(result)
print(index_result)