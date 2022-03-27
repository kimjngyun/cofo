for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  MIN = min(l)
  MAX = max(l)
  print(l.index(MIN)+1, l.index(MAX)+1)