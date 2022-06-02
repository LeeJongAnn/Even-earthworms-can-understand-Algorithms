n = 12345
def solution(n):
    answer = list(str(n))
    result = []
    test2 = []
    for i in range(len(answer)):
        result.append(answer[i])
    result.sort(reverse=True)
    for z in result:
        test2.append(int(z))
    return test2
print(solution(n))