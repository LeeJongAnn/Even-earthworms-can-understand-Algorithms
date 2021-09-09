import  sys
sys.stdin = open("in3.txt","rt")

def DFS(L,sum):
    if sum>s:
        return
    global results
    if L == n:
        if sum>results:
            results = sum
    else:
        DFS(L+1,sum+ch[i])
        DFS(L+1,sum)

if __name__ == "__main__":
    s,n = map(int,input().split())
    ch = [0] * (n+1)
    results = -214700000
    for i in range(n):
        ch[i] = int(input())
    DFS(0,0)
    print(results)




