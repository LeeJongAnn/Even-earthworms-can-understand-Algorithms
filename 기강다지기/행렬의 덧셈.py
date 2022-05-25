
arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
def solution(arr1, arr2):
    for i in range(len(arr1)):
        answer = []
        for j in range(len(arr1[0])):
            answer.append(arr1[i][j] + arr2[i][j])
    return answer
print(solution(arr1,arr2))