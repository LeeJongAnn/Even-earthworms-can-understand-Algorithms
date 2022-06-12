def solution(s):
    result_list = (str(s))
    split = result_list.split(' ')
    first = []
    second = []
    third = []
    answer = ""
    final = []
    first.append(split[0])
    second.append(split[1])
    third.append(split[2])
    for i in first:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += " "
    for b in second:
        for j in range(len(b)):
            if j % 2 == 0:
                answer += b[j].upper()
            else:
                answer += b[j].lower()
        answer += " "

    for c in third:
        for j in range(len(c)):
            if j % 2 == 0:
                answer += c[j].upper()
            else:
                answer += c[j].lower()
    return answer
print(solution("try hello world"))