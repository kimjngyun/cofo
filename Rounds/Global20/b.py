import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  s = input()
  n = len(s)
  t = 0
  flag = True
  for i in range(n):
    if s[i]=='A': t+=1
    else: t-=1
    if t<0: flag = False; break;
  if s[-1] == 'B' and flag: print("YES")
  else: print("NO")