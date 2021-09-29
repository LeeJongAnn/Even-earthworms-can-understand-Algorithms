import sys
sys.stdin = open('in2.txt','r',encoding='utf-8')

n = int(input())

tmp = []
for i in range(n):
    input_data = input().split()
    tmp.append((input_data[0],input_data[1]))

tmp.sort(key=lambda student : student[1])

for student in tmp:
    print(student[0],end=" ")
