seoul = ["Jane", "Kim"]
def solution(seoul):
    index = seoul.index("Kim")
    return "김서방은 " + str(index) + "에 있다"
print(solution(seoul))

# seoul = ["Jane", "Kim"]
# def solution(seoul):
#     for i in range(len(seoul)):
#         if seoul[i] == 'Kim':
#             print("김서방은",i,"에 있다")
#     return
# print(solution(seoul))