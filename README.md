# Even-earthworms-can-understand-Algorithms

Data Structure &amp; Algorithms

<details>
<summary>목차 <- 클릭</summary>

### - 1. 기초 다지기

### - 2. 구현

### - 3. 스택 큐 해쉬

### - 4. Greedy 알고리즘

### - 5. DFS 알고리즘

### - 6. 정렬 알고리즘

### - 7. DP
</details>

## - 기초

> | 기초                                                                                                                                                                                                                                                                       |설명|
> | ------                                                                                                                                                                                                                                                                   |---|
> | 1. 4월 22일 K번째 약수 풀이                                                                                                                                                                                                                                                      |...|  
> | 2. 4월 24일 K번째 수 풀이                                                                                                                                                                                                                                                       |...|
> | 3. 4월 25일 K번째 큰 수 풀이                                                                                                                                                                                                                                                     |...|
> | 4. 4월 27일 정다면체 풀이                                                                                                                                                                                                                                                        |...|
> | 5. 4월 30일 자릿수의 합 풀이                                                                                                                                                                                                                                                      |...|
> | 6. 5월 12일 에라토스테네스의 체                                                                                                                                                                                                                                                     |...|
> | 7. [백준 2475번 검증수 - 10월 16일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EA%B8%B0%EA%B0%95%EB%8B%A4%EC%A7%80%EA%B8%B0/%EA%B2%80%EC%A6%9D%EC%88%98%20-%20%EB%B0%B1%EC%A4%80%202475%EB%B2%88.py)                                   | 간단한 계산 문제|
> | 8. [백준 10871번 X보다 작은 수 - 22년 2월 6일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EA%B8%B0%EA%B0%95%EB%8B%A4%EC%A7%80%EA%B8%B0/X%EB%B3%B4%EB%8B%A4%20%EC%9E%91%EC%9D%80%20%EC%88%98%20-%20%EB%B0%B1%EC%A4%80%2010871%EB%B2%88.py) | 특정 수가 주어지고 X보다 작은 수를 찾는다. |
> | 9. [백준 2587번 곱셈 - 22년 2월 9일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EA%B8%B0%EA%B0%95%EB%8B%A4%EC%A7%80%EA%B8%B0/%EA%B3%B1%EC%85%88%20-%20%EB%B0%B1%EC%A4%80%202588%EB%B2%88.py)                                           | 곱셈의 표현 |
> | 10. [백준 11720번 숫자의 합 - 22년 2월 9일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EA%B8%B0%EA%B0%95%EB%8B%A4%EC%A7%80%EA%B8%B0/%EC%88%AB%EC%9E%90%EC%9D%98%20%ED%95%A9%20-%20%EB%B0%B1%EC%A4%80%2011720%EB%B2%88.py)                | 순차적으로 더해서 나오는 값을 구한다. |
> | 11. [백준 1546번 평균 - 22년 2월 11일]()                | 문제를 잘못 이해해서 헤맸다.. |


***

## - 구현

> | 구현                                                                                                                                                                                                                                                           | 설명                                                                                           |
> |----------------------------------------------------------------------------------------------|-------------------------------------|
> | 1. 회문 문자열 검사 - 5월 11일                                                                                                                                                                                                                                        ||
> | 2. 숫자만 추출 문제 - 5월 14일                                                                                                                                                                                                                                        ||
> | 3. 자리 배치 바꾸기 - 5월 20일                                                                                                                                                                                                                                        | ..                                                                                           |
> | 4. 격자판 최대합 - 5월 20일                                                                                                                                                                                                                                          | ..                                                                                           |
> | 5. 카드 역배치 - 5월 25일                                                                                                                                                                                                                                           | ..                                                                                           |
> | [6. 상하좌우 - 22년 1월 24일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EA%B5%AC%ED%98%84/%EC%83%81%ED%95%98%EC%A2%8C%EC%9A%B0.py)                                                                                       | 좌표를 구성하고 반복문을 돌면서 확인했을때 해당 문자열에 값이면 하나씩 값을 올리거나 빼서 좌표칸을 움직인다.                                |
> | [7. 시각 - 10월 15일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EA%B5%AC%ED%98%84/%EC%8B%9C%EA%B0%81.py)                                                                                                              | 특정 수가 한번이라도 들어가있는 00시 00분 00초를 모두 구하는것                                                       |
> | [8. 백준 18406번 럭키 스트레이트 - 22년 1월 25일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EA%B5%AC%ED%98%84/%EB%9F%AD%ED%82%A4%20%EC%8A%A4%ED%8A%B8%EB%A0%88%EC%9D%B4%ED%8A%B8%20-%20%EB%B0%B1%EC%A4%80%2018406%EB%B2%88.py) | 반으로 나눠서 양옆에 값이 같다는 것을 구해야 한다. 빼게 되면 음수 값이 나오므로 더했을때 0이지만 , 양 옆에 값을 더했을때 왼쪽과 오른쪽이 같다로 풀어도 된다. |
> | [9. 왕실의 나이트 - 22년 1월 23일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EA%B5%AC%ED%98%84/%EC%99%95%EC%8B%A4%EC%9D%98%20%EB%82%98%EC%9D%B4%ED%8A%B8.py)                                                               | 나이트의 움직임을 정의하고 , 움직임을 대입했을때 성립하는 경우를 코드로 정의한다. 그러면 그 중에서 나오는 것이 나이트가 갈 수 있는 길의 개수이다.         |
> | [10. 백준 15686 치킨배달 - 22년 1월 25일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EA%B5%AC%ED%98%84/%EC%B9%98%ED%82%A8%20%EB%B0%B0%EB%8B%AC%20-%20%EB%B0%B1%EC%A4%80%2015686%EB%B2%88.py)                                | 우선 가정 집과 치킨집을 입력받아서 1인 경우 가정집에 저장하고 ,2인 경우 치킨집으로 저장한다. 그리고 치킨집과 가정집 사이의 절대값을 구하여 최소값을 구한다.   |
> | [11. 문자열 재정렬 - 22년 1월 28일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EA%B5%AC%ED%98%84/%EB%AC%B8%EC%9E%90%EC%97%B4%20%EC%9E%AC%EC%A0%95%EB%A0%AC.py)                                                              | 문자열을 입력받아 알파벳이면 리스트에 추가하고 아스키 코드 값의 순서대로 정렬해준다. 그리고 숫자는 더해서 문자열 조인으로 합쳐주면 문자열 재정렬이 완성된다.     |
> | [12. 문자열 압축 - 22년 1월 29일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EA%B5%AC%ED%98%84/%EB%AC%B8%EC%9E%90%EC%97%B4%20%EC%95%95%EC%B6%95.py)                                                                        | 문자열을 입력받았을때 중복되는 경우는 숫자로 치환해준다.                                                              |
> | [13. 백준 3190번 뱀 - 22년 2월 1일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EA%B5%AC%ED%98%84/%EB%B1%80%20-%20%EB%B0%B1%EC%A4%80%203190%EB%B2%88.py)                                                                   | 왜 이렇게 복잡하냐..                                                                                 |
> | [14. 백준 1152번 단어의 개수 - 22년 2월 7일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EA%B5%AC%ED%98%84/%EB%8B%A8%EC%96%B4%EC%9D%98%20%EA%B0%9C%EC%88%98-%20%EB%B0%B1%EC%A4%80%201152%EB%B2%88.py)                          | 문자열이 나올때마다 카운트를 세고 공백이 나오면 카운트를 세는 간단한 방식으로 해결함                                              |
> | [15. 숫자의 개수 - 백준 2577번 - 22년 2월 12일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EA%B5%AC%ED%98%84/%EC%88%AB%EC%9E%90%EC%9D%98%20%EA%B0%9C%EC%88%98%20-%20%EB%B0%B1%EC%A4%80%202577%EB%B2%88.py)                    | 배열을 만들고 해당하는 숫자의 값을 배열에 넣어서 카운트를 올려주면 배열에서 해당 숫자의 개수를 셀 수 있다.                                |
> | [16. 백준 14502번 연구소 - 22년 2월 13일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/DFS%EC%99%80BFS/%EC%97%B0%EA%B5%AC%EC%86%8C%20-%20%EB%B0%B1%EC%A4%80%2014502%EB%B2%88.py)                                                                                                                                                                                                                           | DFS를 이용해서 0인 곳은 바이러스가 퍼지게 만든다.                                                               |
> | [17. 백준 2562번 최댓값 - 22년 2월 15일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EA%B5%AC%ED%98%84/%EC%B5%9C%EB%8C%93%EA%B0%92%20-%20%EB%B0%B1%EC%A4%80%202562%EB%B2%88.py)| ~~맞았는데 왜 틀리는거죠?~~ 인덱스 값을 고쳤더니 됐다.. 뭐지?                                                       |

***

## - 스택 큐 해쉬

> |스택 큐 해쉬|설명|
> |------|---|
> |[1. 가장 큰 수 구하기 (Stack) - 6월 22일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EC%8A%A4%ED%83%9D%20%ED%81%90%20%ED%95%B4%EC%89%AC/Stack%20-%20%EA%B0%80%EC%9E%A5%20%ED%81%B0%20%EC%88%98%20.py)| 새로 들어온 값과 이전에 있던 값을 비교해서 append|
> |2. 큐를 이용한 조세퍼스(Queue) - 6월 22일| .. |
> |3. 막대기 개수 세기(Stack) - 6월 24일|.. |
> |4. 응급환자 순서 정하기(Queue) - 6월 26일|..|
> |5. 교육과정설계(Queue) - 6월 26일 |..|
> |6. 안 쓰인 단어 찾기(Hash) - 6월 27일|..|
> |7. 애니그램(Hash) - 6월 28일 |..|

## - Greedy 알고리즘

***
> | Greedy 알고리즘                                                                                                                                                                                                                                                                                  | 설명                                                                                  | 
> |-------------------------------------------------------------------------------------|-------------------------| 
> | [1. 회의실 사용하기 - 6월 30일     ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%ED%9A%8C%EC%9D%98%EC%8B%A4%20%EB%B0%B0%EC%A0%95.py)                                                                                                     | 시간 순서상 뒷자리와 앞자리가 이어지도록 만든다                                                          |
> | [2. 출전할 씨름선수 구하기 - 6월 30일     ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EC%94%A8%EB%A6%84%EC%84%A0%EC%88%98%20%EC%84%A0%EB%B0%9C%ED%95%98%EA%B8%B0.py)                                                                      | 튜플 자료형에 몸무게를 비교해서 갱신하고 카운트를 센다                                                      |
> | [3. 창고 정리하기 - 7월 10일     ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EC%B0%BD%EA%B3%A0%EC%A0%95%EB%A6%AC.py)                                                                                                                  | 맨 앞과 맨 뒤를 최대와 최소로 놓고 서로 빼준다                                                         |
> | [4. 타이타닉에서 살아남기 - 8월 3일     ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%ED%83%80%EC%9D%B4%ED%83%80%EB%8B%89%EC%97%90%EC%84%9C%20%EC%82%B4%EC%95%84%EB%82%A8%EA%B8%B0.py)                                                      | 정렬한 후 가장 몸무게가 많은 사람과 가장 적은 사람을 더해서 보트 무게 제한보다 큰지 작은지를 따진다                           |
> | [5. 증가수열 - 10월 13일     ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EC%A6%9D%EA%B0%80%EC%88%98%EC%97%B4.py)                                                                                                                    | 왼쪽과 오른쪽을 번갈아가면서 뽑고 마지막에 뽑은값과 비교하여 수열에 집어넣는다 while 문을 이용하고 왼쪽끝과 오른쪽 끝을 lt 와 rt로 선언한다 |
> | [6. 역수열 - 10월 13일     ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EC%97%AD%EC%88%98%EC%97%B4.py)                                                                                                                              | 1부터 순서대로 앞에 빈자리가 있어야 하고 항상 자기보다 큰 수가 앞에 오는 것이다.                                     |
> | [7. 백준 11047 동전으로 지불하기     ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EB%8F%99%EC%A0%84%EC%9C%BC%EB%A1%9C%20%EC%A7%80%EB%B6%88%ED%95%98%EA%B8%B0%20%EB%B0%B1%EC%A4%80%2011047%EB%B2%88.py)                                   | K로 나눈 몫을 더하되 , 나머지를 다시 값으로 집어넣어서 다음번에 나눌때 나머지를 다음 동전으로 나눌 수 있도록 해준다.                |
> | [8. 백준 1541 잃어버린 괄호 - 8월 15일 (출처:https://pacific-ocean.tistory.com/228)     ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EC%9E%83%EC%96%B4%EB%B2%84%EB%A6%B0%20%EA%B4%84%ED%98%B8%20-%20%EB%B0%B1%EC%A4%80%201541%EB%B2%88.py) | 문자열을 사칙연산자를 기준으로 쪼갠다.                                                               |
> | [9. 백준 11399번 ATM - 22년 1월 26일     ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/ATM%20-%20%EB%B0%B1%EC%A4%80%2011399%EB%B2%88.py)                                                                                               | 수를 정렬하고 난 다음 그 뒤로 값을 연속해서 더해주도록 구성한다.                                               |
> | [10. 백준 5585번 일본판 거스름돈 구하기 - 8월 19일     ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EA%B1%B0%EC%8A%A4%EB%A6%84%EB%8F%88%20%EC%9D%BC%EB%B3%B8%ED%8C%90%20-%20%EB%B0%B1%EC%A4%80%205585%EB%B2%88.py)                            | 일본판 동전구하기 처음에 입력값이 하나밖에 없어서 평소대로 동전 리스트 만들고 지불한 금액 넣어서 했는데 안돼서 그냥 읽는거 말고 자체 코드로 작성함 |
> | [11. 백준 13305번 주유소에 기름넣고 가기 - 10월 9일     ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EC%A3%BC%EC%9C%A0%EC%86%8C%20-%20%EB%B0%B1%EC%A4%80%2013305%EB%B2%88.py)                                                                 | 첫번째 도시에서 무조건 기름을 넣어야 된다는게 중요한 포인트이다.                                                |
> | [12. 백준 2839번 설탕배달 - 22년 1월 25일 (출처:https://ooyoung.tistory.com/81)     ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EC%84%A4%ED%83%95%EB%B0%B0%EB%8B%AC%20-%20%EB%B0%B1%EC%A4%80%202839%EB%B2%88.py)                          | if문을 통해서 나머지가 안남는경우를 5kg 봉지 개수를 구하고 만약에 아닌 경우에는 -3을 빼고 3kg 짜리 봉지를 하나 추가하며 반복문을 돈다.  |
> | [13. 큰 수의 법칙 - 22 년 1월 23일     ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%ED%81%B0%20%EC%88%98%EC%9D%98%20%EB%B2%95%EC%B9%99.py)                                                                                             | 가장 큰 수와 두번째로 큰 수를 찾는다 . 큰 수를 먼저 c만큼 더하고 반복이 끝나면 두번째 큰 수를 더해준다                       |
> | [14. 숫자 카드 게임 - 9월 28일    ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EC%88%AB%EC%9E%90%20%EC%B9%B4%EB%93%9C%20%EA%B2%8C%EC%9E%84.py)                                                                                         | 라인 별로 정렬해서 가장 작은 수를 찾고 그 작은 수에서 가장 큰 수를 찾는다.                                        |
> | [15. 1이 될 때까지 - 22년 1월 23일     ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/1%EC%9D%B4%20%EB%90%A0%EB%95%8C%EA%B9%8C%EC%A7%80.py)                                                                                               | 처음 수를 5로 나누었을때 나머지 값이 생기면 1을 빼고 다시 5로 나누어준다. 이 과정을 카운트를 센다.                         |
> | [16. 백준 4796번 캠핑 - 10월 16일     ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EC%BA%A0%ED%95%91%20-%20%EB%B0%B1%EC%A4%80%204796%EB%B2%88.py)                                                                                     | 8번에서 5번만 연속해서 캠핑하므로 반복문으로 돌면서 계산해준다                                                 |
> | [17. 백준 2217번 로프 - 10월 20일 ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EB%A1%9C%ED%94%84%20-%20%EB%B0%B1%EC%A4%80%202217%EB%B2%88.py)                                                                                         | 답안 수정                                                                               |
> | [18. 모험가 길드 - 22년 1월 21일 ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EB%AA%A8%ED%97%98%EA%B0%80%EA%B8%B8%EB%93%9C.py)                                                                                                         | 겁의 크기를 하나씩 올리면서 값을 비교하고 만약 겁의 크기가 크면 겁의 값을 초기화 해서 다시 센다                             |
> | [19. 곱하기 아니면 더하기 - 22년 1월 21일    ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EA%B3%B1%ED%95%98%EA%B8%B0%EC%95%84%EB%8B%88%EB%A9%B4%EB%8D%94%ED%95%98%EA%B8%B0.py)                                                             | 가장 큰 수를 만들기 위해서는 첫번째 값이 항상 더하기여야 한다. 그리고 나머지 값은 곱하기로 하면 가장 큰 값이다.                   |
> | [20. 백준 1439번 문자열 뒤집기 - 10월 22일    ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EB%AC%B8%EC%9E%90%EC%97%B4%20%EB%92%A4%EC%A7%91%EA%B8%B0.py)                                                                                   | 0 과 1을 교환해준다.                                                                       |
> | [21. 만들 수 없는 금액 - 22년 1월 24일    ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EB%A7%8C%EB%93%A4%20%EC%88%98%20%EC%97%86%EB%8A%94%20%EA%B8%88%EC%95%A1.py)                                                                       | 가지고 있는 수는 존재한다고 생각하고 오름차순으로 순서대로 놓고 더하면 각각의 숫자가 만들어진다.                              |
> | [22. 볼링공 고르기 - 22년 1월 24일    ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EB%B3%BC%EB%A7%81%EA%B3%B5%20%EA%B3%A0%EB%A5%B4%EA%B8%B0.py)                                                                                         | 각 무게에 해당하는 볼링공을 배열로 만들어 개수를 구한다. A가 어느 한 공을 선택하면 전체 개수에서 그 공을 뺴주고 나머지를 더해주어야 한다     |
> | [23. 백준 1715번 카드 정렬하기 - 10월 21일    ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EC%B9%B4%EB%93%9C%20%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0%20-%20%EB%B0%B1%EC%A4%80%201715%EB%B2%88.py)                                          | 풀 수 있을것 같았는데..                                                                      |
> | [24. 백준 1789번 수들의 합 - 10월 23일    ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EC%88%98%EB%93%A4%EC%9D%98%20%ED%95%A9%20-%20%EB%B0%B1%EC%A4%80%201789%EB%B2%88.py)                                                              | 200이 안되는데?                                                                          |
> | [25. 백준 10162번 전자레인지 - 10월 28일    ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EC%A0%84%EC%9E%90%EB%A0%88%EC%9D%B8%EC%A7%80%20-%20%EB%B0%B1%EC%A4%80%2010162%EB%B2%88.py)                                                      | 답안수정 (뭥미..)                                                                         |
> | [26. 백준 1026번 보물 - 22년 1월 28일    ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/%EB%B3%B4%EB%AC%BC%20-%20%EB%B0%B1%EC%A4%80%201026%EB%B2%88.py)                                                                                   | 곱해서 가장 작은 수를 만들어야 한다. 대신 두번째 배열은 정렬해서는 안된다. 그렇다면?                                   |
> | [27. 백준 10610번 30 - 22년 2월 6일    ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/Greedy%20Algorithms/30%20-%20%EB%B0%B1%EC%A4%80%2010610%EB%B2%88.py)                                                                                                 | ~~맞는데 왜 틀리지??? (맞왜틀?)~~ -1을 출력하는 과정에서 문제가 발생했는데 해결함                                 |
> | [28. 백준 1946번 신입사원 선발 - 22년 1월 30일    ]()                                                                                                                                                                                                                                                    | 첫번째 입력과 두번쨰 입력을 받아서 리스트를 만들었는데 두개를 합치는 과정을 다시 해봐야 할 것 같다.                           |


## - DFS/BFS

***
> | DFS/BFS                                                                                                                                                                                                                                                                               | 설명                                                       |
> | ----------------------------------------------------------                                                                                                                                                                                                                            |---|
> | [1.부분집합 구하기 - 9월 6일    ]()                                                                                                                                                                                                                                                            | 사용하느냐 사용하지 않느냐를 따지면서 상태트리를 따라서 내려간다.                     |
> | [2.합이 같은 부분집합 - 9월 6일    ]()                                                                                                                                                                                                                                                          | 총 합에서 상태트리를 따라 내려가면서 일부를 뺐을때 값이 같으면 그때를 YES로 출력한다.       |
> | [3.강아지 데리고 타기 (cut-Edge) - 9월 9일   ]()                                                                                                                                                                                                                                                | 전체 경우의 수를 다 따지지 않고 합계가 무게 제한을 넘는 경우를 커트해준다.              |
> | [4.중복순열 - 9월 17일    ]()                                                                                                                                                                                                                                                               | 한개의 노드에 차수가 여러개이므로 반복문을 사용하여 돌아간다.                       |
> | [5.조합 - 9월 28일    ]()                                                                                                                                                                                                                                                                 | 중복을 허용하지 않고 뽑으므로 1개씩 더해주면 된다.                            |
> | [6.백준 2798번 블랙잭 - 10월 14일   ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EC%99%84%EC%A0%84%ED%83%90%EC%83%89/%EB%B8%94%EB%9E%99%EC%9E%AD%20-%20%EB%B0%B1%EC%A4%80%202798.py)                                                                | 정답에 근접한 것 같은데 시간초과에 걸림, 불필요한 계산을 줄일 방법을 생각해봐야 될 듯        |
> | [7. 백준 18352번 특정 거리의 도시 찾기 - 22년 2월 8일 ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/DFS%EC%99%80BFS/%ED%8A%B9%EC%A0%95%20%EA%B1%B0%EB%A6%AC%EC%9D%98%20%EB%8F%84%EC%8B%9C%20%EC%B0%BE%EA%B8%B0%20-%20%EB%B0%B1%EC%A4%80%2018352%EB%B2%88.py) | 1에서 시작하며 1과 연결되어 있는 곳 중에서 거리가 2인 곳을 찾는다. 방문한 지역에 1을 더해준다 |
> | [8. 백준 18405번 경쟁적 전염 - 22년 2월 19일 ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/171d98fa2d3793ec7a95ab0ab52c4ed614df9c35/DFS%EC%99%80BFS/%EA%B2%BD%EC%9F%81%EC%A0%81%20%EC%A0%84%EC%97%BC%20-%20%EB%B0%B1%EC%A4%80%2018405%EB%B2%88.py)                                                                                                                                                                                                                                                 | 작은 수부터 바이러스가 퍼져나간다. |
> | [9. 백준 2606번 - 바이러스 - 22년 2월 24일 ](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/d70ceccd54d7bf5a6fd2026f671a81e6d463dd58/DFS%EC%99%80BFS/%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4%20-%20%EB%B0%B1%EC%A4%80%202606%EB%B2%88.py)  | 간단한 DFS문제 ,1로부터 연결된 모든 컴퓨터를 출력해준다. |

## - 정렬

***
> | 정렬 알고리즘                                                                                                                                                                                                                                                       |설명|
> | ------                                                                                                                                                                                                                                                        |---|
> | [1.위에서 아래로 - 9월 29일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EC%A0%95%EB%A0%AC/%EC%9C%84%EC%97%90%EC%84%9C%20%EC%95%84%EB%9E%98%EB%A1%9C.py)                                                                     | 기초적인 정렬 문제이다 . 숫자를 내림차순으로 정렬한다.|
> | [2.성적이 낮은 순서로 출력하기 - 9월 29일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EC%A0%95%EB%A0%AC/%EC%84%B1%EC%A0%81%EC%9D%B4%20%EB%82%AE%EC%9D%80%20%EC%88%9C%EC%84%9C%EB%A1%9C%20%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0.py) | 점수대로 정렬하고 그와 이어진 이름을 출력한다. 파이썬 문법에 대해서 알아야 한다.|
> | [3. 백준 1181번 단어정렬 - 22년 2월 15일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EC%A0%95%EB%A0%AC/%EB%8B%A8%EC%96%B4%20%EC%A0%95%EB%A0%AC%20-%20%EB%B0%B1%EC%A4%80%201181%EB%B2%88.py)                                   | 리스트에 길이에 관한 정보와 문자를 집어넣고 수를 길이에 관한 정보로 정렬해준다. 그럼 순서대로 정렬됨 , 중복 제거도 들어가야함  |
> | [4. 백준 1427번 - 소트인사이드 - 22년 2월 16일](https://github.com/LeeJongAnn/Even-earthworms-can-understand-Algorithms/blob/master/%EC%A0%95%EB%A0%AC/%EC%86%8C%ED%8A%B8%EC%9D%B8%EC%82%AC%EC%9D%B4%EB%93%9C%20-%20%EB%B0%B1%EC%A4%80%201427%EB%B2%88.py)                                                                                                                                                                                                                         | 거꾸로 정렬해주는 간단한 문제  |
> | [5. 백준 11650번 - 좌표정렬 - 22년 2월 27일]()  | 이것도 간단하다..  |


## - DP

***
> | DP 알고리즘                                                               | 설명                                                                  |
> | --------------------------------------------------------------------- |------|
> | [1.백준 1463번 1로 만들기 - 22년 2월 9일 ]()                                    | ~~좀 더 생각해봐야할듯...?~~ 해봐도 안되네 ㅋㅋㅋ 카운트 횟수를 줄이려면 큰 값으로 먼저 계산하는게 맞는것 같다. |
> | [2.백준 9261번 LCS(Longest Common Subsequence) - 22년 2월 24일 ]()| 답은 맞았는데 왜 틀리죠..? |
