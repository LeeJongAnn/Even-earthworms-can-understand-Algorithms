def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x

def lcm(x,y):
    result=(x*y)//gcd(x,y)
    return result

def solution(n, m):
    answer = []
    answer.append(gcd(n,m))
    answer.append(lcm(n,m))
    return answer
print(solution(3,12))
