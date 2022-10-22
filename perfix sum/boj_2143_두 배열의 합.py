import imp
import sys
input = sys.stdin.readline
from itertools import accumulate as acc

t = int(input().strip())
n = int(input().strip())
a = list(map(int,input().split()))
m = int(input().strip())
b = list(map(int,input().split()))

a_acc = [0] + list(acc(a))
b_acc = [0] + list(acc(b))

print(a_acc)
print(b_acc)