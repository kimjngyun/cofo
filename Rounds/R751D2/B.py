import sys
from collections import Counter
input = sys.stdin.readline

def trans(l):
    cd = Counter(l)
    t = [0] * len(l)
    for i in range(len(l)):
        t[i] = cd[l[i]]
    return t

def findAll(l):
  ret = []
  ret.append(l)
  while l!=trans(l):
    l = trans(l)
    ret.append(l)
  return ret

t = int(input())
for _ in range(t):
  n = int(input()) # Size of Array
  a = list(map(int, input().split())) # Array

  pre = findAll(a)
  qn = int(input()) # Number of Queries
  for _ in range(qn):
    x, k = map(int, input().split()) #Query
    if k>=len(pre)-1:
      print(pre[len(pre)-1][x-1])
    else:
      print(pre[k][x-1])