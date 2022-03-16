import sys
input=sys.stdin.readline
for _ in range(int(input())):
  n, k, x = map(int,input().split())
  s = list(input().rstrip())
  l = []
  cnt = 0
  for i in range(n):
    if s[i]=="*": 
      cnt += 1; 
    else:
      if cnt>0: l.append(cnt*k+1)
      cnt = 0
  if cnt>0: l.append(cnt*k+1)

  l.reverse()
  ans = []
  x -= 1

  for i in range(len(l)):
    ans.append((x%l[i]))
    x //= l[i]
  ans.reverse()

  flag = True
  idx = 0
  for i in range(len(s)):
    if s[i]=="a": print("a", end=''); flag=True
    else:
      if flag: print("b"*ans[idx], end=''); idx+=1; flag = False
  print()