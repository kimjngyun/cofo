import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  n, k = list(map(int, input().split()))
  b = 1
  c = 1
  h = 0
  flag = True
  while True:
    if c >= n:
      flag = False
      break
    c += b
    h += 1
    if b*2 > k:
      b = k
      break
    else:
      b = b*2
  if flag:
    l = n-c
    h += l//b
    if l % b != 0:
      h += 1
  print(h)