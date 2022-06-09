s = "a234"
def solution(s):
    answer = True
    if (len(s) == 6 or len(s) == 4) and s.isdigit() == True:
        return True
    else:
        return False
print(solution(s))
