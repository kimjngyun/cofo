import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  l = list(map(int ,input().split()))
  MAX = 0
  for i in range(n):
    MAX = max(l[i]-i-1, MAX)
  print(MAX)