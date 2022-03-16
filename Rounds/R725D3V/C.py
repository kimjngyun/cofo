import sys
from bisect import bisect_left, bisect_right
input=sys.stdin.readline
for _ in range(int(input())):
  n, l, r = map(int,input().split())
  arr = list(map(int, input().split()))
  arr.sort()
  cnt = 0
  for i in range(n-1):
    if arr[i]+arr[i+1]>r: continue # possible min 
    if arr[i]+arr[-1]<l: continue # possible max
    left = bisect_left(arr, l-arr[i], i+1, n)
    right = bisect_right(arr, r-arr[i], i+1, n)
    cnt+=right-left
  print(cnt)
