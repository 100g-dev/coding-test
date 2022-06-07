# 그래프 이론 Graph
- 서로 다른 개체(혹은 객체)가 연결되어 있는 경우 고려해야 할 알고리즘
<br></br>

**‼️ 그래프 구현 방식**
|  |구현 방법|메모리 공간|비용 계산 시간|
|:-------:|:-----------:|:-----:|:-----:|
|인접 행렬</br>Adjacency Matirx|2차원 배열을 사용|$O(V^2)$|$O(1)$|
|인접 리스트</br>Adjacency List|리스트 사용|$O(E)$|$O(V)$|   
   
    
---
## 서로소 집합 자료구조 Union-find [↗️](https://github.com/100g-dev/Coding_Test/tree/main/Graph/disjoint.py)
- 트리 자료구조를 이용하여 서로소 집합(공통 원소가 없는 두 집합)을 표현
- union( ) : 각 원소의 루트 노드 A, B를 찾아 A를 B의 부모로 설정 (일반적으로 A<B)
- find( ) : 재귀적으로 부모 노드를 탐색 → 경로 압축(Path compression)으로 시간복잡도 개선
- ‼️ 원소를 노드로 갖고, union 연산을 간선으로 갖는 그래프로 표현이 가능
</br> → 서로소 집합을 이용하여 그래프의 사이클 판별이 가능[↗️](https://github.com/100g-dev/Coding_Test/tree/main/Graph/cycle.py)
<br></br>

## 신장 트리 Spannin Tree [↗️](https://github.com/100g-dev/Coding_Test/tree/main/Graph/kruskal.py)
- 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
- **크루스칼 알고리즘(Kruskal Algorithm)** : 최소 신장 트리를 구하는 그리디 알고리즘
- 시간복잡도 : $O(ElogE)$
<br></br>

## 위상 정렬 Topology Sort [↗️](https://github.com/100g-dev/Coding_Test/tree/main/Graph/topology_sort.py)
- 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
- 시간복잡도 : $O(V+E)$
<br></br>
---
### 1. 팀 결성 [↗️](https://github.com/100g-dev/Coding_Test/tree/main/Graph/team.py)
- 0번부터 n번까지 n+1개의 팀이 존재할 때, (1)팀 합치기 와 (2)같은 팀 여부 확인 연산을 수행할 수 있다.
- m개의 연산을 수행할 때 (2)번 연산에 대한 결과를 출력하는 프로그램을 작성하여라.
<br></br>

### 2. 도시 분할 계획 [↗️](https://github.com/100g-dev/Coding_Test/tree/main/Graph/city_plan.py)
- n개의 집과 집을 연결하는 m개의 길이 있다. 마을을 분리할 때, 각 마을 안의 집들은 서로 연결되어 있어야한다.
- 분리된 마을 간의 길과 마을 안에서 불필요한 길을 없애 비용을 아끼려고 할 때, 최소 유지비를 구하여라.
<br></br>

### 3. 커리큘럼 [↗️](https://github.com/100g-dev/Coding_Test/tree/main/Graph/curri.py)
- 1번부터 n번까지의 강의에 걸리는 시간과 선수 과목이 주어질 때, 각 과목마다 수강하기까지 걸리는 최소 시간을 구하여라.
<br></br>

---
<div align="right"><a href="https://github.com/100g-dev/Coding_Test">메인 화면으로 ↩</a></div>
