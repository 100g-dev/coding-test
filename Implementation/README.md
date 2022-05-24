# 구현 Implementation
- 모든 범위의 코딩 테스트 문제 유형을 포함 - 완전 탐색(Brute Force)와 시뮬레이션(Simulation)
- 많은 제한 조건, 지나치게 긴 코드, 소수점 출력, 문자 파싱 등 구현이 까다로운 유형
<br></br>  

**‼️ 메모리 제약 사항/ 채점 환경 고려**
- C/C++은 변수 표현 범위 고려
- 파이썬에서 크기가 1000만 이상인 리스트는 용량 제한
- 파이썬은 C/C++보다 느린 동작 속도 -> Pypy3 이용(가능할 때)

---
### 1. 상하좌우 [↗](https://github.com/100g-dev/Coding_Test/blob/0d5b31eb0a6ed431e321b6d7f23fd525c0769195/Implementation/udlr.py)
- 1\*1 크기의 정사각형으로 이뤄진 n\*n공간에서 U, D, L, R 중 하나의 문자가 입력될 때 해당 방향으로 이동
- (1, 1)에서 출발할 때, 최종 도착 지점의 좌표를 출력하여라.(단, 이동이 불가한 경우는 무시)
<br></br>  

### 2. 시각 - 계산[↗](https://github.com/100g-dev/Coding_Test/blob/0d5b31eb0a6ed431e321b6d7f23fd525c0769195/Implementation/time3.py), 문자열[↗](https://github.com/100g-dev/Coding_Test/blob/0d5b31eb0a6ed431e321b6d7f23fd525c0769195/Implementation/time3_string.py)
- 00시 00분 00초부터 n시 59분 59초까지 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수를 구하여라. (단, 0 <= n <= 23) 
<br></br>  

### 3. 왕실의 나이트 [↗](https://github.com/100g-dev/Coding_Test/blob/0d5b31eb0a6ed431e321b6d7f23fd525c0769195/Implementation/knight.py)
- 8*8 체스판에서 나이트의 위치가 주어졌을 때 이동할 수 있는 경우의 수를 구하여라. 
<br></br>  

### 4. 게임 개발 [↗](https://github.com/100g-dev/Coding_Test/blob/0d5b31eb0a6ed431e321b6d7f23fd525c0769195/Implementation/game_dev.py)
- n*m의 지도에서 (A, B)의 위치가 주어질 때, 다음 룰에 맞춰 캐릭터가 방문할 수 있는 칸의 개수를 출력하여라.
    1. 현재 위치, 방향 기준으로 왼쪽 방향부터 차례대로 이동 방향을 정한다.
    2. 해당방향에 칸이 존재하면 해당 칸으로 이동, 없으면 회전만 수행
    3. 네 방향이 모두 이미 가본 칸이거나 바다인 경우 방향을 유지한 채로 한 칸 뒤로 이동하고 1단계 반복, 뒤가 바다인 경우 종료
