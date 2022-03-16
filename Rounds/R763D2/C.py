import sys
input=sys.stdin.readline
  
for _ in range(int(input())):
  n = int(input())
  arr = list(map(int, input().split()))
  poss = [0] * n
  for i in range(2, n):
    poss[i] = arr[i]//3
  poss += [0, 0]
  # possible max
  pm = [0] * n
  for i in range(n):
    pm[i] = arr[i]+poss[i+1]+2*poss[i+2]
  print(pm)
  