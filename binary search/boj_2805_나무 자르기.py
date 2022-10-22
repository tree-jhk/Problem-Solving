import sys
input = sys.stdin.readline
n,m = map(int,input().split())
t = list(map(int,input().split()))
lt,rt,mid,answer = 0,max(t),0,-1
def summ(h):
    tmp = 0
    for tt in t:
        if tt > h:
            tmp += (tt - h)
    return tmp
while(lt<=rt):
    mid = (lt+rt) // 2
    if summ(mid) >= m:
        answer = max(answer,mid)
        lt = mid + 1
    else:
        rt = mid - 1
print(answer)