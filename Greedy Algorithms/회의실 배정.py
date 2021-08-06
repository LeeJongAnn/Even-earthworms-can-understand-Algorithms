import sys
sys.stdin = open("in1.txt","rt")

n = int(input())
meeting = []
cnt = 0
for i in range(n):
    s,e=map(int,input().split())
    meeting.append((s,e))
meeting.sort(key=lambda x:(x[1],x[0]))
print(meeting)
et=0

for x,y in meeting:
    if x>=et:
        et=y
        cnt+=1
print(cnt)

