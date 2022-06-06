# 이진탐색 Binary Search
- 정렬되어 있는 데이터의 시작점과 끝점을 기준으로 중간점의 데이터를 반복적으로 비교해 원하는 데이터를 탐색
- 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편에 속한다.
- **재귀함수**[↗](https://github.com/100g-dev/Coding_Test/blob/main/Binary_search/recursive_bs.py) 또는 **반복문**[↗](https://github.com/100g-dev/Coding_Test/blob/main/Binary_search/iteration_bs.py)을 이용
<br></br>  
---
### 1. 부품 찾기 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Binary_search/find_parts.py)
- 고유한 정수 번호를 가진 부품이 n개 있을 때, 손님이 m개 종류의 부품의 견적서를 요구했을 때 부품이 있으면 yes를, 없으면 no를 출력하여라.
- **➕ 다른 풀이 : [계수정렬](https://github.com/100g-dev/Coding_Test/blob/main/Binary_search/find_parts_count.py), [집합 자료형](https://github.com/100g-dev/Coding_Test/blob/main/Binary_search/find_parts_set.py)**
<br></br>  
### 2. 떡볶이 떡 만들기 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Binary_search/ricecake.py)
- 떡볶이 떡의 길이가 일정하지 않을 때, 절단기의 높이(h)보다 긴 떡은 위의 부분이 잘린다. 손님이 m 길이만큼 떡을 요청했을 때, 절단기에 설정할 수 있는 높이의 최댓값을 구하여라.
- 파라메트릭 서치(Parametric Search): 최적화 문제를 결정 문제로 바꾸어 해결
