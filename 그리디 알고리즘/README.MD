## 그리디 알고리즘 예제 1 

  1. 동전 분류하기 
    - 100원짜리 동전과 50원짜리 동전 10원짜리 동전 1원 짜리 동전이 있을때 
      361원을 분류하시오. (동전을 가장 적게 사용하여)
      
    - 그렇다면 100원 동전과 50원 짜리 동전 10원짜리 동전 1원짜리 동전을 코드로 만들고 큰 순서대로 나누면 될 것 같다.
  - 파이썬 
  
    import os 

    num = 371
    
    coin_type = [100,50,10,1]
    
    for i in range(4):
    
      cnt = num /coin_type[i]
      
      print(cnt)
  - C++ 
  
    #include <iostream>

using namespace std;

int n = 362;

int cnt = 0;

int coinTypes[4] = {100, 50, 10,1};

int main() {

    for (int i = 0; i < 4; i++) {
    
        int coin = coinTypes[i];
        
        cnt += n / coin;
        
        n %= coin;
    
	}
    cout << cnt << '\n';
}
   
