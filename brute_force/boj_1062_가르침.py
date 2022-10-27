import sys
input = sys.stdin.readline
from itertools import combinations as combi

n, k = map(int, input().split())
words = [input().strip() for _ in range(n)]

answer = 0

k -= 5
if k < 0:
    print(0)
    exit(0)
for i in range(n):
    words[i] = (words[i][4:] + words[i][:-4])
    tmp = set(words[i]) - set('antic')
    if len(tmp) == 0:
        answer += 1
    else:
        words[i] = tmp
words = list(map(''.join, words))
candi = set(''.join(words))

# print(words)
for cb in combi(candi,k):
    cnt = 0
    letters = ''.join(cb)
    for word in words:
        for l in word:
            if l not in letters:
                break
        else:
            cnt += 1
    answer = max(answer, cnt)
print(answer)