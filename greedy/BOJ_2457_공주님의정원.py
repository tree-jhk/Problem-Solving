import sys
input = sys.stdin.readline
from itertools import accumulate
from collections import deque
from heapq import *

days = list(accumulate([0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]))

n = int(input())
f = []
for _ in range(n):
    a = list(map(int, input().split()))
    st = days[a[0] - 1] + a[1]
    en = days[a[2] - 1] + a[3]
    f.append([st, en, en - st])
f = deque(sorted(f, key=lambda x: (x[0], x[1])))
st = days[2] + 1
en = days[10] + 30
answer = 0

# while 종료 조건 주의 (등호 들어가야하는지)
while(st <= en):
    # 가장 큰 것 추출: heap 가능할려나
    candi = []
    while(f and f[0][0] <= st):
        tmp = f.popleft()
        tmp[2] -= st
        heappush(candi, (-tmp[2], tmp))
    answer += 1
    st = candi[0][1][1]
    # 꽃이 지는 날짜 == st인 경우도 빼야함.
    while(1):
        for i in range(len(f)):
            if f[i][1] <= st:
                del f[i]
                break
        else:
            break
    if len(f) == 0: break
print(answer if st > en else 0)