# 다이나믹 프로그래밍 Dynamic Programming
- 메모리 공간을 약간 더 사용하여 연산 속도를 비약적으로 증가시키는 방법
- 큰 문제를 작게 나누고, 같은 문제는 한 번씩만 풀어 문제를 효율적으로 해결 -> **분할정복 Divide and Conquer**
<br></br>  

---
## 탑다운 Top-Down [↗](https://github.com/100g-dev/Coding_Test/blob/main/Dynamic_programming/top_down.py)
- 재귀 함수를 이용 -> 메모이제이션(Memoization)
- 큰 문제를 해결하기 위해 작은 문제를 호출하는 하향식 방법
<br></br>  

## 보텀업 Bottom-Up [↗](https://github.com/100g-dev/Coding_Test/blob/main/Dynamic_programming/bottom_up.py)
- 반복문을 이용 - 결과를 DP 테이블에 저장
- 작은 문제부터 차근차근 답을 도출하는 상향식 방법
<br></br>

**‼️ 오버헤드 발생**
- 재귀 함수를 이용하는 탑다운 방식의 경우 함수를 호출하는 과정에서 메모리 상에 적재되는 오버헤드가 발생
- 재귀 함수 대신 반복문을 이용하면 오버헤드를 줄일 수 있어, 일반적으로 성능이 더 좋다.
<br></br>
---
### 1. 1로 만들기 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Dynamic_programming/make_1.py)
- 정수 x가 주어질 때, 아래의 4가지 연산을 선택하여 1로 만든다. 이 때, 연산을 사용하는 최솟값을 구하여라.
  1. x가 5로 나누어 떨어지면, 5로 나눈다.
  2. x가 3으로 나누어 떨어지면, 3으로 나눈다.
  3. x가 2로 나누어 떨어지면, 2로 나눈다.
  4. x에서 1을 뺀다.
- $a_i = min(a_{i-1},\ a_{i/2},\ a_{i/3},\ a_{i/5}) + 1$
<br></br>  

### 2. 개미 전사 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Dynamic_programming/ant_fighter.py)
- 일직선의 식량창고를 선택적으로 약탈할 때, 서로 인접한 식량창고가 공격받으면 상대가 알아차릴 수 있다.
- 식량창고 n개에 대한 정보가 주어졌을 때, 얻을 수 있는 식량의 최댓값을 구하여라.
- $a_i = max(a_{i-1},\ a_{i-2}+k_i)$
<br></br>

### 3. 바닥 공사 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Dynamic_programming/floor.py)
- 가로 길이가 n, 세로 길이가 2인 직사각형의 바닥에 1x2, 2x1, 2x2 덮개를 이용하여 채울 때, 바닥을 채울 수 있는 모든 경우의 수를 구하여라.
- $a_i = a_{i-1}\ +\ a_{i-2}*2 $
<br></br>

### 4. 효율적인 화폐 구성 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Dynamic_programming/effect_money.py)
- n가지 종류의 화폐를 이용하여 합이 m원이 되도록 구성할 때, 최소한으로 사용할 수 있는 화폐 개수를 구하여라. (불가능한 경우는 -1)
- $a_i = min(a_i,\ a_{i-k}+1)\ \ $  (단, $a_{i-k}$를 만드는 방법이 없을 때, $a_i = 10001$)
<br></br>
