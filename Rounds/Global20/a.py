import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  if not (sum(l)-n)%2==0: print('errorgorn')
  else: print('maomao90')
  