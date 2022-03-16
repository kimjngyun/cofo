import sys
input=sys.stdin.readline
def solve(i, j, arr):
  ret = 0
  for t in range(len(arr)):
    if t!=i and t!=j:
      if (t-i)*(arr[j]-arr[i])==(j-i)*(arr[t]-arr[i]): ret+=1
  return ret


for _ in range(int(input())):
  n = int(input())
  arr = list(map(int, input().split()))
  ans = 100
  if n<=2: print(0); continue
  for i in range(n):
    for j in range(i+1, n):
      r = solve(i, j, arr)
      ans = min(ans, n-r-2)
  
  print(ans)
