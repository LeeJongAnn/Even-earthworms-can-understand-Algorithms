import sys
sys.stdin = open("in15.txt","rt")
a = input()
answer = 1e9
for step in range(1,len(a)//2+1):
    compressed = ""
    prev = a[0:step]
    count = 1
    for j in range(step,len(a),step):
        if prev == a[j:j + step]:
            count +=1
            print("이전의 수 : ",prev)
            print("압축 가능 카운트: ", count)
        else:
            compressed += str(count) + prev if count >=2 else prev
            prev = a[j:j + step]
            count = 1
            print("압축문자열 : " ,compressed)
    compressed += str(count) + prev if count >= 2 else prev
    answer = min(answer,len(compressed))
print(answer)
