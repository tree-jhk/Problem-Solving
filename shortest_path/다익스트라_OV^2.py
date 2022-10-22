import sys
input = sys.stdin.readline
INF = int(1e9)

# n: 정점 개수 m: 간선 개수
n, m = map(int,input().split())
# start: 시작 정점
start = int(input().strip())
# graph: 정점 i와 연결된 정점들을 담는 2차원 list
graph = [[] for i in range(n + 1)]
# 해당 정점 방문 여부 -> 각 정점 한번씩 탐색하고, 
# 탐색할 때마다 인접 노드까지의 거리(distance[node])가 이전보다 짧으면 갱신
visited = [False] * (n + 1)
# 0번: 무시 -> 0번을 굳이 두는 이유는, input에서 첫번째 정점에 대한 표시로 1을 했기 때문
# (n + 1)을 할지 n을 할지는 input에 따라 다름
# 1번부터 카운팅 -> 모두 INF로 초기화
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a 정점과 인접한 정점 b를 이어주고 그때의 간선 가중치 c를 함께 저장
    graph[a].append((b, c))

# 현재까지 방문하지 않은 곳들 중 저장된 최단거리가 가장 짧은 노드 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if not visited[i] and (distance[i] < min_value):
            min_value = distance[i]
            index = i
    return index

# O(v^2)의 시간 복잡도 코드
def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    # j[0]: 인접 정점
    # j[1]: start에서 j[0] 정점까지의 거리
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드의 최단거리는 이미 distance[start] = 0(자기 자신까지 거리)로 초기화됨
    # 따라서 시작 정점을 제외하고 출발
    for _ in range(n - 1):
        # 매 loop마다 현재까지 방문하지 않은 곳들 중 저장된 최단거리가 가장 짧은 노드(now) 반환
        now = get_smallest_node()
        # 방문할 노드에 대해 방문 처리
        visited[now] = True
        # j[0]: 인접 정점
        # j[1]: start에서 j[0] 정점까지의 거리
        for j in graph[now]:
            # distance[now]: 여태까지 발견된, start 정점에서 now 정점으로 가는 거리들 中 가장 작은 값
            # cost = (start 정점 -> now 정점 까지의 최단 거리) + (now 정점 -> j[1] 정점까지의 거리)
            cost = distance[now] + j[1]
            # start에서 j[0]까지 가는데, now 정점을 거치는 것이 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    # 출력할 내용:
    # 정점 start -> 정점 i 까지의 최단 거리: distance[i]
    if distance[i] != INF:
        print(f"node {start} -> node {i} shortest path: {distance[i]}")
    else:
        print(f"node {start} -> node {i} impossible to reach")

"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
정점 1 -> 정점 1 까지의 최단 거리: 0
정점 1 -> 정점 2 까지의 최단 거리: 2
정점 1 -> 정점 3 까지의 최단 거리: 3
정점 1 -> 정점 4 까지의 최단 거리: 1
정점 1 -> 정점 5 까지의 최단 거리: 2
정점 1 -> 정점 6 까지의 최단 거리: 4
"""