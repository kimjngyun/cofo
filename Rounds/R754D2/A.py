import sys
input=sys.stdin.readline
for _ in range(int(input())):
  l = list(map(int, input().split()))
  if sum(l)%3: print(1)
  else: print(0)
  
