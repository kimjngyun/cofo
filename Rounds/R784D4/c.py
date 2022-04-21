import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  flag = True

  for i in range(0, n, 2):
    if l[i]%2!=l[0]%2: flag=False; break;
  
  for i in range(1, n, 2):
    if l[i]%2!=l[1]%2: flag=False; break;
  if flag: print("YES")
  else: print("NO")
