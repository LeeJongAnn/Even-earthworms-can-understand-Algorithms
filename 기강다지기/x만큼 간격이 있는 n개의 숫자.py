def solution(x, n):
    answer = []
    result = 1
    for i in range(1,n+1):
        result =x*i
        answer.append(result)
    return answer

print(solution(2,5))