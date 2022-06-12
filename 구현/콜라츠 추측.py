def solution(num):
    count = 0
    while num:
        if num == 1:
            break
        if count == 500:
            break
        if num % 2 == 0:
            num = num // 2
            count += 1
        else:
            num = (num * 3) + 1
            count +=1
    return count if count != 500 else -1
print(solution(626331))
# def solution(num):
#     answer = 0
#     while num>1:
#         while num%2==0:
#             num//=2
#         if num % 2 != 0:
#             num = (num*3) + 1
#     return num
