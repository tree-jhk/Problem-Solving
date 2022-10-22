import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# n: 정점 개수 m: 간선 개수
n, m = map(int,input().split())
# start: 시작 정점
start = int(input().strip())
# graph: 정점 i와 연결된 정점들을 담는 2차원 list
graph = [[] for i in range(n + 1)]
# 0번: 무시 -> 0번을 굳이 두는 이유는, input에서 첫번째 정점에 대한 표시로 1을 했기 때문
# (n + 1)을 할지 n을 할지는 input에 따라 다름
# 1번부터 카운팅 -> 모두 INF로 초기화
# distance는 1번~n번 index번째 정점의 최단 거리를 저장함
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a 정점과 인접한 정점 b를 이어주고 그때의 간선 가중치 c를 함께 저장
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # q에 출발 지점 입력
    # 이렇게 초기화해야 첫 loop 돌아가는 것을 고려해서 전체 loop랑 통합시킴
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        # 이전 loop에서 갱신된 노드들을 heappop
        # now: 거쳐갈 노드
        # dist: 여태 발견된 start -> now까지의 최단경로
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 노드이면 무시
        # 등호 처리하면 안되는 이유: 처리 이후에는 distance[now] == dist인 상황이기 때문.
        if distance[now] < dist:
            continue
        # i[0]: target 노드
        # start -> i[0]까지의 최단거리를 구하려함
        for i in graph[now]:
            # cost: start -> now -> i[0]까지의 최단거리
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
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
node 1 -> node 1 shortest path: 0
node 1 -> node 2 shortest path: 2
node 1 -> node 3 shortest path: 3
node 1 -> node 4 shortest path: 1
node 1 -> node 5 shortest path: 2
node 1 -> node 6 shortest path: 4
"""