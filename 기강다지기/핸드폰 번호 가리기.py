phone_number = "027778888"

def solution(phone_number):
    answer = len(phone_number)
    result = []
    for i in range(answer-4):
        phone_number = phone_number.replace(phone_number[i],'*',1)
    return phone_number
print(solution(phone_number))