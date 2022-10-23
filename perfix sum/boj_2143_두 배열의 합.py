import sys
input = sys.stdin.readline
from itertools import accumulate as acc
from itertools import combinations as combi
import bisect as bs

t = int(input().strip())
n = int(input().strip())
a = list(map(int,input().split()))
m = int(input().strip())
b = list(map(int,input().split()))
answer = 0

a_ = sorted([cb[1] - cb[0] for cb in combi([0] + list(acc(a)), 2)])
b_ = sorted([cb[1] - cb[0] for cb in combi([0] + list(acc(b)), 2)])
for i in range(len(a_)):
    l = bs.bisect_left(b_, t - a_[i])
    r = bs.bisect_right(b_, t - a_[i])
    answer += (r - l)

print(answer)