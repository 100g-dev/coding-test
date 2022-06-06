# 최단 경로 Shortest Path
- 가장 짧은 경로를 찾는 알고리즘
- 한 지정메서 다른 특정 지점까지의 최단 경로를 계산
- 모든 지점에서 다른 모든 지점까지의 최단 경로를 계산
<br></br>
---
## 다익스트라 알고리즘 Dijkstra Algorithm
- 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구하는 그리드 알고리즘
- ❗️음의 간선이 없을 때, 정상적으로 동작 → GPS 소프트웨어의 기본 알고리즘
  ### 1. 간단한 다익스트라  [↗](https://github.com/100g-dev/Coding_Test/blob/main/Shortest_path/simple_dijkstra.py)
  - 1차원 리스트를 이용하여 단계마다 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택
  - 시간복잡도 : $O(V^2)$
  ### 2. 개선된 다익스트라  [↗](https://github.com/100g-dev/Coding_Test/blob/main/Shortest_path/enhance_dijkstra.py)
  - 최단 거리가 가장 짧은 노드를 선택하는 과정을 우선순위 큐를 이용하는 방식으로 대체
  - 시간복잡도 : $O(Elog{V})$
  <br></br>  

## 플로이드 워셜 알고리즘 Floyd-Warshall Algorithm [↗](https://github.com/100g-dev/Coding_Test/blob/main/Shortest_path/floyd_warshall.py)
- 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구하는 다이나믹 프로그래밍 알고리즘
- $D_{ab} = min(D_{ab}\ ,\ D_{ak}+D_{kb})$
- 시간복잡도 : $O(N^3)$
<br></br>

## 벨만포드 알고리즘 Bellman-Ford Algorithm [↗](https://github.com/100g-dev/Coding_Test/blob/main/Shortest_path/bellman_ford.py)
- 음수 간선이 포함된 경우에 한 노드에서 다른 노드로 가는 각각의 최단 경로를 구하는 알고리즘
- ❗️단, 음의 사이클이 존재하는 경우에는 동작하지 않는다. 
- 시간복잡도 : $O(VE)$
<br></br>
---
### 1. 미래 도시 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Shortest_path/future_city.py)
- 양방향으로 연결된 미래 도시에서, 1번에서 출발하여 k번을 방문하여 x번으로 가려고 할 때, 최소 이동 시간을 출력하여라. (도시 간 이동 시간은 1)
- n이 한정적이고 구현이 간단 → 플로이드 워셜
<br></br>  

### 2. 전보 [↗](https://github.com/100g-dev/Coding_Test/blob/main/Shortest_path/mail.py)
- 다른 도시로 전보를 보내기 위해서 도착 도시 방향으로 향하는 통로가 필요하고, 전달하는데 일정 시간이 소요된다.
- 도시 c에서 위급 상황이 발생하여 최대한 많은 도시로 전보를 보낼 때, 전보를 받을 수 있는 도시 개수와 모든 도시들이 메시지를 받는데까지 걸린 시간을 구하여라.
- n과 m 범위가 매우 크고, 도시 간 최단 거리 → 개선된 다익스트라
---

<div align="right"><a href="https://github.com/100g-dev/Coding_Test">메인 화면으로 ↩</a></div>
