for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  l.sort()

  if n==1:
    if l[0]>1: print("NO")
    else: print("YES")
  else:
    if l[n-1]>l[n-2]+1: print("NO")
    else: print("YES")