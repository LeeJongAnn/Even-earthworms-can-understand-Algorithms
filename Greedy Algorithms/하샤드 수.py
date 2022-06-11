def solution(x):
    arr = list(str(x))
    answer = 0
    for i in range(len(arr)):
        answer += int(arr[i])
    if int((''.join(arr)))%answer == 0:
        return True
    else:
        return False
print(solution(18))