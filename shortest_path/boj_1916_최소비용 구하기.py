import heapq as hq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input().strip())
m = int(input().strip())
# 도시 번호가 1부터 시작하기 때문에 n + 1
g = [[] for _ in range(n + 1)]
# start, end, 비용 -> 가중치가 있는 단방향 그래프
for _ in range(m):
    s, e, c = map(int,input().split())
    g[s].append((e,c))
for i in range(n + 1):
    g[i].sort()
# 출발점, 도착점
start, end = map(int,input().split())
# 최단거리를 저장할 distance 배열, 도시 번호가 1부터 시작하기 때문에 n + 1
# 무한값으로 지정하는 이유는, 최소인 값으로 갱신하기 위해
# start에서 출발할 때 기준으로의 최단 거리임
distance = [INF] * (n + 1)

def dijkstra(start):
    distance[start] = 0
    q = []
    hq.heappush(q,(0,start))
    while(q):
        dist, now = hq.heappop(q)
        # 이 경우는 맨 처음에 distance가 INF로 초기화 되어 있을 때만 발생한다.
        # now 기준 탐색 여부를 확인함
        if distance[now] < dist:
            continue
        # info[0]: target 정점
        # info[1]: now -> info[0]으로 바로 가는 거리
        # cost: start -> now -> info[0]
        for info in g[now]:
            cost = distance[now] + info[1]
            # start -> info[0]까지 가는 최단 거리보다 짧은 최단 거리를 발견하면 갱신
            if distance[info[0]] > cost:
                distance[info[0]] = cost
                hq.heappush(q,(cost, info[0]))

dijkstra(start)
print(distance[end])