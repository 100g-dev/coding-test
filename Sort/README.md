# 정렬 Sort
- 데이터를 특정한 기준에 따라 순서대로 나열하는 것
    1. 정렬 라이브러리 이용
    2. 정렬 알고리즘 원리 -> 선택, 삽입, 퀵 정렬 등
    3. 더 빠른 정렬 -> 계수 정렬 등
<br></br>  

---
## 선택 정렬 Selection Sort [↗](https://github.com/100g-dev/Coding_Test/blob/main/Sort/selection_sort.py)
- 첫 번째 인덱스부터 가장 작은 데이터를 선택하여 바꾸는 과정을 반복하여 정렬
- 시간복잡도 : O(N<sup>2</sup>)
<br></br>  

## 삽입 정렬 Insertion Sort[↗](https://github.com/100g-dev/Coding_Test/blob/main/Sort/insertion_sort.py)
- 데이터가 들어갈 적절한 위치를 찾아 삽입
- **데이터가 거의 정렬되어 있을 때 매우 빠르게 동작**
- 시간복잡도 : O(N<sup>2</sup>)
<br></br>

## 버블 정렬 Bubble Sort [↗](https://github.com/100g-dev/Coding_Test/blob/main/Sort/bubble_sort.py)
- 서로 인접한 두 원소를 비교하여 정렬
- 시간복잡도 : O(N<sup>2</sup>)
<br></br>  

## 퀵 정렬 Quick Sort[↗](https://github.com/100g-dev/Coding_Test/blob/main/Sort/quick_sort.py)
- 피벗을 설정하고, 피벗을 기준으로 큰 데이터와 작은 데이터의 위치를 변경
- 시간복잡도 : O(NlogN)
<br></br>

## 계수 정렬 Count Sort [↗](https://github.com/100g-dev/Coding_Test/blob/main/Sort/count_sort.py)
- 데이터의 크기 범위가 정수 형탵로 제한된 경우에만 사용 가능하지만 매우 빠른 정렬 알고리즘
- 비교기반의 정렬이 아닌 모든 범위를 담을 수 있는 크기의 리스트를 선언하여 사용
- 시간복잡도 : O(N+K)  (K는 데이터 최댓값 크기)
<br></br>  

## ➕ 파이썬 정렬 알고리즘
- 기본 정렬 알고리즘 : sorted()
- 리스트 객체 내장 함수 : sort()
- 시간복잡도 : O(NlogN)
<br></br>  
---
### 1. 위에서 아래로 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Sort/updown.py)
- 크기 상관없이 나열되어 있는 수를 큰 수부터 작은 수 순서대로 정렬하여라.
<br></br>  

### 2. 성적 출력 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Sort/grade.py)
-n명의 학생 이름과 성적 정보가 입력될 때, 성적이 낮은 순서로 학생 이름을 출력하여라.
---

<div align="right"><a href="https://github.com/100g-dev/Coding_Test">메인 화면으로 ↩</a></div>
