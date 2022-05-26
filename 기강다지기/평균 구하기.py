
arr = [1,2,3,4]

def solution(arr):
    answer = 0
    array1 = []
    for i in range(len(arr)):
        array1.append(arr[i])
        answer += array1[i]
    print(array1)
    answer = answer/len(arr)
    return answer

print(solution(arr))