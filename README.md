# Even-earthworms-can-understand-Algorithms
Data Structure &amp; Algorithms

# 목차 - 기초 다지기  
### - [1.K번째 약수 해설](#K번째-약수-해설)  
### - [2.자릿수의 합 해설](#자릿수의-합-해설)  
### - [7.에라토스테네스의 체 만들기](#에라토스테네스의-체-만들기)  
### - [8.숫자만 추출 문제](#8.숫자만-추출-문제)



# Data-Structure and Algorithms
- 기초 다지기

> 1. 4월 22일 K번째 약수 풀이 - 4월 29일 해설 추가 
> 2. 4월 24일 K번째 수 풀이
> 3. 4월 25일 K번째 큰 수 풀이
> 4. 4월 27일 정다면체 풀이
> 5. 4월 30일 자릿수의 합 풀이 - ~~4월 30일 해설 작성 중 ..~~ 작성완료
> 6. 5월 12일 에라토스테네스의 체 공부 - 5월 13일 해설 작성 중 

***

- 탐색과 시뮬레이션

> 1. 회문 문자열 검사 공부 - 5월 11일
> 7. 5월 14일 숫자만 추출 문제 공부 - 5월 14일 해설 작성 중 


# Data Structure &amp; Algorithms




# K번째 약수 해설


> 입력값이 8 4 일 때 8의 약수 중에서 4번째 값을 구하는 문제이다 
그렇다면 어떻게 구해야 될까? 우선은 8의 약수들을 구해야 된다.

### 1) 첫번째 할 일 8의 약수 구하기

---

8의 약수를 구하기 위해서는 다음과 같은 식이 필요하다  

    for i in range(1,n): -> 반복문이 돌면서 1부터 자기 자신까지 돌아간뒤 
    
    if n % i == 0: -> n을 1부터 8의 숫자까지 한번씩 나누어서 0이 되는 수를 구한다
       
    cnt+= 1 -> 0이 되는 값을 cnt 라는 변수에 저장한뒤 하나씩 증가시킨다

---

### 2) 두번째 할 일 8의 4번째 약수를 구하기

> 여기서 이제 약수의 값을 구하는 것은 끝이 났다. 그렇다면 4번째의 약수는 어떻게 구해야 할까?

---

우리는 cnt라는 변수를 하나 생성해서 0으로 떨어질 때마다 
값을 하나씩 카운트 해서 올렸다.

그러면 그 값이 구하려는 K값과 일치하면 cnt값이 
k번째 값을 구한다는 것을 알 수 있다.

그러면 코드로 써보면 

    if cnt == k: -> 하나씩 증가된 cnt 값이 k값과 일치한다면

    print(i) -> 해당하는 i번째를 출력한다. 즉 i가 8일 때는 cnt값이 계속 증가돼서 4가 되게 되고
                4는 k값과 일치하므로 즉 4번째 약수는 8이 된다는 것을 알 수 있다.

이렇게 나타낼 수 있겠다.   
전체 코드는 다음과 같다.   
>import sys  
>sys.stdin = open("in1.txt", "rt")  
>n,k = map(int, input().split())  
cnt = 0  
for i in range(1,n+1):  
    if n%i == 0:  
        cnt += 1  
    if cnt == k:  
        print(i)  
        break  
else:  
    print(-1)



---




# 자릿수의 합 해설 

> 1. 다음과 같은 입력값이 주어질 때 각 자리수의 합을 구하는 문제이다   
> 125 15232 97 
---

> 자릿수가 저렇게 주어졌을때 각 자리수는 어떻게 될지 보면   
> 125 - > 8  
> 12532 - > 13   
> 97 - > 16   
> 이런식으로 문제가 나와야 한다. (각 자리수를 구하는 것이므로)
***
그렇다면 이제 문제를 이해했으므로 풀이를 생각해보자   
각 자리의 숫자는 어떻게 구해야될까? 

### ***바로 나눗셈으로 각 자리 숫자를 구할 수 있다.***

> 예를 들어서 125를 10으로 나누게 되면 몫은 12가 되고 나머지는 5가 된다.   
> 여기서 남은 12를 다시 10으로 나누게 되면 몫은 1이 되고 나머지는 2가 된다.   
> 그리고 다시 이 과정을 반복해주면 나머지는 1이 되며 1 , 2 , 5 의 값을 따로 구할 수 있게 되는 것이다.   
> 이것을 이용하여 각 자리 숫자를 구해준다.

***
앞에서 말한 내용을 코드로 구현하면 아래와 같다  

> def digit_sum(x):  
    sum = 0  
    while x > 0:  
        sum += x % 10  
        x = x // 10  
    return sum  
![img.png](img.png)

***
그러면 이제 자릿수의 합을 구하는 함수를 구했으니   
이제 이 중에서 가장 큰 값들을 구하는 함수를 구해야 한다.   
각각 구한 값들을 어떤 변수에 담고 ,   
max값을 어떤 특정 값으로 설정한 다음 반복문이 돌아가면서 비교한   
값과 max값을 비교하여 반복문에서 구한 값이 더 크다면 max값에 집어넣어준다.  
코드로 표현하면 아래와 같다
> for x in a:  
    tot = digit_sum(x)  
    if tot > max:  
        max = tot  
        res = x    

3   
125 15232 97가 입력값일때 자릿수의 합이 최대값인 수는 97이다

![img_1.png](img_1.png)


전체 코드는 아래와 같다.  
> import sys

>sys.stdin = open("in5.txt", "r")  

>n = int(input())  
a = list(map(int, input().split()))  
res = 0  
max = -2147000000  

>def digit_sum(x):  
    sum = 0  
    while x > 0:  
        sum += x % 10  
        x = x // 10  
    return sum  
for x in a:  
    tot = digit_sum(x)  
    if tot > max:
        max = tot
        res = x
>print(res)

자릿수의 합 해설 끝

# 에라토스테네스의 체 만들기
 

1부터 특정 수까지 있다고 할 때 그러면 소수는 어떻게 구해야 될까?
그러면 소수라는 것은 또 무엇일까?  
이 문제는 고대 그리스의 에라토스테네스[^에라토스테네스]라는 사람이 
고안해낸 방법으로   
이번 시간에는 이와 같은 의문에 대해서 
알아보고 코드로 구현해 보겠다. 

*** 

> 이 문제를 풀기 전에 우선은 소수에 대해서 알아야 한다.  
소수는 1과 자기 자신만을 약수로 갖는 수이다.  
보통의 수들은 예를 들어 6의 약수를 보면 1,2,3,6 이런 식으로 여러 개로 나뉘어 질 수 있다.  
하지만 소수는 오직 1과 자기 자신만을 약수로 갖는 외로운 수인 것이다. 
![https___blogs-images forbes com_neilhowe_files_2019_05_TW_All_the_Lonely_People_WEB](https://user-images.githubusercontent.com/50771738/118070845-9f815980-b3e1-11eb-8b11-eddb9d0600cb.png)

***
* 그렇다면 1부터 20까지 소수의 개수를 구하기 위에선 다음과 같은 작업이 필요하다  
    1. 1부터 20까지의 숫자를 인덱스로 갖는 배열 ch가 있다고 가정한다.  
    2. 각 숫자의 배수를 반복문을 통해서 cnt 값에 +1을 해준다 그러면   
    배열에 숫자마다 각각의 약수가 1로 표시가 된다.
    3. 그리고 if문을 통해서 ch가 인덱스 별로 돌 때 각각에 저장되어 있는 값이 0인 경우  
    소수라는 것을 알 수 있다.
    4. 즉 0인 경우는 소수로 표기하고 0이 아닌 경우는 소수가 아니다라고 표기하면 된다.    
    
### 그러면 코드로 구현해보도록 하겠다.

> n = int(input()) -> 숫자를 읽어들인다. 예를 들어서 20    
> ch = [0] * [n+1] - > ch배열의 인덱스를 읽어들인 숫자로 초기화 해준다.  
> for i in range(2,n+1):  
>   cnt+=1  
>   if ch[i]!=0:  
>       print("# %d NO" %(i+1))  
>   for j in range(i,n+1,i):  
>       
>       
>       
# 8.숫자만 추출 문제       

***

이번 문제는 문자열과 숫자가 섞여있는 어떤(?) 글이 있을때  
이곳에서 숫자만 추출해내는 알고리즘에 관한 문제이다.  
예를 들어서 g0en2Ts8eSoft 이런 이상한 문자열이 있다고 하자
그렇다면 여기서 어떻게 숫자들만 쏙쏙 뽑아낼 수 있을까? 

> #### 1. g0en2Ts8eSoft 이 문자열을 각각의 낱개의 글자로 나열한다
> #### 2. 그런 다음 반복문을 통해서 돌면서 각각의 글자가 숫자인지 문자인지 판별하게 한다.
> #### 3. 뽑아낸 숫자들을 뭉쳐서 하나의 수로 만든다.
> #### 4. 그 수에서 약수를 구하고 약수의 개수를 센다. (본래 문제가 이거였음)

#### * 위와같은 순서로 문제를 풀어나가면 된다. 
       


***   
[에라토스테네스]: 에라토스테네스(Ερατοσθένης, 기원전 274년 ~ 기원전 196년)는 고대 그리스의 수학자이자 천문학자이다. 헬레니즘 시대 이집트에서 활약했으며, 문헌학 및 지리학을 비롯해 헬레니즘 시대 학문 다방면에 걸쳐 업적을 남겼지만, 특히 수학과 천문학의 분야에서 후세에 남는 큰 업적을 남겼다.
