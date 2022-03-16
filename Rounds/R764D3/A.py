for _ in range(int(input())):
  n = int(input())
  arr = list(map(int, input().split()))
  MAX = max(arr)
  MIN = min(arr)
  print(MAX-MIN)