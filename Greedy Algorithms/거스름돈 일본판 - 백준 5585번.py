import sys
sys.stdin = open('in11.txt','rt')
n = int(input())
coin_list = [1,5,10,50,100,500]
provide = 1000 - n
coin_list.sort(reverse=True)
results = 0
for i in coin_list:
    results+= provide//i
    provide%=i
print(results)
