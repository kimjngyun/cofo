import sys
input=sys.stdin.readline
def solve(n, k, arr):
  arr.sort(reverse=True)
  score = sum(arr)-sum(arr[:2*k])

  t = 1
  counter = []
  for i in range(1, 2*k):
    if arr[i]!=arr[i-1]: counter.append(t); t=1;
    else: t+=1
    if i==2*k-1: counter.append(t)

  if counter: score += max(max(counter)-k , 0)
  return score

for _ in range(int(input())):
  n, k = map(int,input().split())
  arr = list(map(int, input().split()))
  print(solve(n, k, arr))