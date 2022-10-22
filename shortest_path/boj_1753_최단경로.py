import heapq as hq
import sys
input = sys.stdin.readline
INF = int(1e9)

# n: 정점 개수 m: 간선 개수
n, m = map(int,input().split())
# start: 시작 정점
s = int(input().strip())
g = [[] for _ in range(n + 1)]
cost = [INF] * (n + 1)
for _ in range(m):
    u, v, w = map(int,input().split())
    g[u].append([w, v])
            
for i in range(1, n + 1):
    g[i].sort()

def dijkstra(s):
    q = []
    cost[s] = 0
    hq.heappush(q,(0,s))
    while(q):
        c, now = hq.heappop(q)
        if cost[now] < c:
            continue
        # info[0]: now -> info[1]까지 갈 때 cost
        # info[1]: target 정점
        for info in g[now]:
            # c: s -> now -> info[1] 거리
            c_ = c + info[0]
            # 이전까지 s -> info[1] 발견한 최단 거리와 비교
            if c_ < cost[info[1]]:
                cost[info[1]] = c_
                hq.heappush(q,(c_, info[1]))

dijkstra(s)

for i in range(1, n + 1):
    if cost[i] == INF:
        print('INF')
    else:
        if i == s:
            print(0)
        else:
            print(cost[i])