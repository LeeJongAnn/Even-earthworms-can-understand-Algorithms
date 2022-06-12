def solution(x):
    answer = 0
    result = list(str(x))
    print(result)
    for i in result:
        answer += int(i)
    if x % answer == 0:
        return True
    else:
        return False
print(solution(19))


# def solution(x):
#     arr = list(str(x))
#     answer = 0
#     for i in range(len(arr)):
#         answer += int(arr[i])
#     if int((''.join(arr)))%answer == 0:
#         return True
#     else:
#         return False
# print(solution(18))