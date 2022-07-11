# 탐색 DFS/BFS
- 많은 양의 데이터 중에 원하는 데이터를 찾는 과정
- 그래프, 트리 등의 자료구조 안에서 탐색을 하는 문제를 주로 다룸
<br></br>  

**➕ 재귀함수**
- 자기 자신을 다시 호출하는 함수
- 재귀의 최대 높이를 초과하지 않도록 변경
  ```python
  import sys
  limit_number = 15000 #기본 3000
  sys.setrecursionlimit(limit_number)
  ```
---
## DFS(Depth-First Search) [↗](https://github.com/100g-dev/Coding_Test/blob/main/Search/dfs.py)
- 깊이 우선 탐색
- 스택 또는 재귀함수를 이용하여 그래프의 깊은 부분부터 우선적으로 탐색
<br></br>  

## BFS(Breadth-First Search)[↗](https://github.com/100g-dev/Coding_Test/blob/main/Search/bfs.py)
- 너비 우선 탐색
- 큐를 이용하여 정점에 가까운 노트부터 탐색
<br></br>

**‼️ DFS/BFS 선택**
- 모든 정점을 방문하는 것이 중요한 문제 -> DFS, BFS
- 경로의 특징을 저장해야 하는 문제/ 검색 대상 그래프가 매우 큰 경우 -> DFS
- 최단 거리/ 대상 규모가 크지 않고 시작 지점에서 목표 대상이 가까운 경우 -> BFS 
<br></br>
---
### 1. 음료수 얼려먹기 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Search/ice.py)
- n*m 크기의 얼음틀에 칸막이는 1, 얼음칸은 0으로 표시되어 있을 때, 생성되는 총 아이스크림의 개수를 구하여라
- 모든 정점 방문 -> DFS/BFS
<br></br>  

### 2. 미로 탈출 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Search/maze.py)
- n*m 크기의 미로에서 (1, 1)의 위치에서 출구인 (n, m)으로 이동해야 한다. 괴물이 있는 부분은 0으로 없는 부분은 1로 표시될 때, 움직여야 하는 최소칸의 개수를 구하여라.
- 최단경로 -> BFS
---
<br></br>
## 기출문제

### Q15. 특정 거리의 도시 찾기 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Search/q15.py)
- BOJ18352
- 입력: 도시의 개수 n, 도로 개수 m, 최단 거리 k, 출발 도시 번호 x
- 출력: 최단 거리가 k인 도시의 개수 (단, 도시가 없다면 -1)
<br></br>
---

<div align="right"><a href="https://github.com/100g-dev/Coding_Test">메인 화면으로 ↩</a></div>
