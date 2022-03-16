import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  l = list(map(int, input().split()))
  if n&1==0: print("YES")
  else:
    flag = True
    for i in range(1, n):
      if l[i]<=l[i-1]:
        flag = False
        print("YES")
        break
    if flag: print("NO")
