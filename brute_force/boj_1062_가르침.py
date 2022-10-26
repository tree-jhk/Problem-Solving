import sys
input = sys.stdin.readline

n, k = map(int, input().split())
words = [input().strip() for _ in range(n)]

k -= 5
if k < 0:
    print(0)
    exit(0)
for i in range(n):
    words[i] = (words[i][4:] + words[i][:-4])
    tmp = set(words[i]) - set('antic')
    words[i] = tmp
words = list(map(''.join, words))
print(words)