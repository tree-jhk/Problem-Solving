import sys
input = sys.stdin.readline
global d, rule

def ch(m):    
    global d, rule
    cnt = 0
    for (st, e, c) in rule:
        if st <= m:
            tmp = e if m > e else m
            cnt += ((tmp - st)//c + 1)
    return cnt >= d

n, k, d = map(int, input().split())
rule = [list(map(int, input().split())) for _ in range(k)]
s, e, answer = 0, n, 0
while(s<e):
    m = (s+e)//2
    if ch(m):
        answer = m
        e = m
    else:
        s = m + 1
print(answer)