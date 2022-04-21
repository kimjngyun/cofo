import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n = int(input())
  s = input()
  c = 0
  idx = 0
  while idx<n:
    if s[idx]=='(': 
      if idx==n-1: break
      idx+=2; c+=1
    elif s[idx]==')':
      t = idx+1
      flag = False
      while t<n:
        if s[t]==')': flag = True; break;
        t+=1
      if flag: 
        c+=1
        idx=t+1
      else:
        break
  print(c, n-idx)