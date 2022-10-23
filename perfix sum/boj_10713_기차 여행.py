import sys
input = sys.stdin.readline
from itertools import accumulate

n, m = map(int,input().split())
path = list(map(lambda x: int(x) - 1, input().split()))
info = [list(map(lambda x: int(x), input().split())) for _ in range(n - 1)]
perfix = [0] * n

for a, b in zip(path[:-1],path[1:]):
    if a > b:
        a, b = b, a
    perfix[a] += 1
    perfix[b] -= 1
print(sum([min(price[0] * cnt, price[1] * cnt + price[2])\
    for price, cnt in zip(info, accumulate(perfix))]))