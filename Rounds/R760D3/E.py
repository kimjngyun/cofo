import sys
input=sys.stdin.readline
def solve(n , arr):
  if n==1: return arr
  d = n*(n+1)//2
  if sum(arr)%d != 0: return []
  s = sum(arr)//d
  ret = []
  temp = arr[n-1]+s-arr[0]
  if temp%n != 0: return []
  else: ret.append(temp//n)

  for i in range(n-1):
    temp = arr[i]+s-arr[i+1]
    if temp%n != 0: return []
    else: ret.append(temp//n)
  
  return ret

  
for _ in range(int(input())):
  n = int(input())
  arr = list(map(int, input().split()))
  t = solve(n, arr)
  if t and min(t)>0: 
    print("YES")
    for i in range(len(t)):
      print(t[i], end=' ')
    print()
  else: print("NO")