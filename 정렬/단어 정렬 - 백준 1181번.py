import sys
sys.stdin = open("in3.txt", 'rt')
n = int(input())
tmp = []
new_tmp = []
for i in range(n):
    num = input()
    count = len(num)
    tmp.append((count,num))
print(tmp)
for x in tmp:
    if x not  in new_tmp:
        new_tmp.append(x)
print(new_tmp)
new_tmp.sort()
for i in range(len(new_tmp)):
    print(new_tmp[i][1])