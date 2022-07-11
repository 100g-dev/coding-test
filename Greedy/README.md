# 탐욕법 Greedy
- 현재 상황에서 가장 좋은 것을 고르는 방법
- 문제 풀이를 위한 최소한의 아이디어를 떠올릴 수 있는 창의력 요구
- 그리디 알고리즘의 해법이 정당한지 검토해야 한다.
<br></br>  
---
### 1. 거스름돈 문제 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Greedy/change.py)
- 거스름돈이 n원일 때 거슬러 주어야 하는 동전의 최소 개수를 구하여라. (단, n은 항상 10의 배수)
- 시간복잡도 : O(k)  (k는 화폐의 종류)
<br></br>  
### 2. 큰 수의 법칙 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Greedy/large_number_rule.py)
- 다양한 수로 이루어진 배열에서 주어진 수를 m번 더하여 가장 큰 수를 만드는 법칙
- 단, 배열 특정 인덱스에 해당하는 수가 연속해서 k번을 초과해 더해질 수 없다.
<br></br>  
### 3. 숫자 카드 게임 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Greedy/card_game.py)
- n*m 배열로 놓여있는 숫자 카드 중 가장 높은 숫자가 쓰인 카드를 뽑는 게임
- 뽑고자 하는 카드가 포함되어 있는 행을 선택한 후, 해당 행의 카드 중 가장 숫자가 낮은 카드를 선택
- 행에서 가장 낮은 숫자를 뽑을 것을 고려하여 전략을 세워야 한다.
<br></br>  
### 4. 1이 될 때까지 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Greedy/until1.py)
- 어떤 수 n이 1이 될 때까지 아래의 두 과정을 반복적으로 선택하여 수행할 때, 최소 횟수를 구하여라.
  1. n에서 1을 뺀다.
  2. n을 k로 나눈다. (단, 나누어 떨어질 때만 선택 가능)
---
<br></br>
## 기출문제

### Q01. 모험가 길드 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Greedy/q01.py)
- 입력: 모험가의 수 n, 각 모험가의 공포도 값 (1 <= n <= 100000)
- 출력: 여행을 떠날 수 있는 그룹 수의 최댓값
<br></br>
### Q02. 곱하기 혹은 더하기 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Greedy/q02.py)
- 입력: 여러 개의 숫자로 이뤄진 하나의 문자열
- 출력: 만들어질 수 있는 가장 큰 수
### Q03. 문자열 뒤집기 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Greedy/q03.py)
- BOJ 1439
- 입력: 0과 1로만 이루어진 문자열
- 출력: 문자열을 0 또는 1로만 만들기 위해서 뒤집어야 하는 횟수
<br></br>
### Q04. 만들 수 없는 금액 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Greedy/q04.py)
- 입력: 동전의 개수 n과 n개의 화폐 단위
- 출력: 동전들로 만들 수 없는 양의 정수 
---
<div align="right"><a href="https://github.com/100g-dev/Coding_Test">메인 화면으로 ↩</a></div>
