def solution(absolutes,signs):
    answer = 0
    # for absolute in absolutes:
    #     print(absolute,end=" ")
    #
    # for sign in signs:
    #     print(sign,end=" ")
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer
print(solution([1,2,3],["false","false","true"]))


# from collections import defaultdict
#
# signs = ["true", "false", "true"]
#
# def solution(absolutes, signs):
#     result = defaultdict(list)
#
#     for sign in signs:
#         print(sign,end=" ")
#
#     for absolute in absolutes:
#         result[absolute].append(sign)
#     return result.values()
#
#
# print(solution([4,7,12],signs))
