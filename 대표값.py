import sys
sys.stdin = open("in5.txt", 'rt')

n = int(input())
a = list(map(int , input().split()))

average = round(sum(a)/n)
min = 21470000

for index , x in enumerate(a):

    tmp = abs(x-average)
    if tmp<min:
        min = tmp
        score=x
        res=index+1
    elif tmp == min:
        if x>score:
            score=x
            res=index+1

print(average,res)




