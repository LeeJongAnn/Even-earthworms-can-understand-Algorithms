def solution(num):
    answer = 0
    while num>1:
        while num%2==0:
            num//=2
            if num % 2 != 0:
                num = (num*3) + 1
    return num
print(solution(6))