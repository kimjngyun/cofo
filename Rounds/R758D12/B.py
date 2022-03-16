import sys
input=sys.stdin.readline
for _ in range(int(input())):
  n, a, b = map(int,input().split())
  if abs(a-b)>1 or a+b>n-2: print(-1); continue
  core = []
  if a==0 and b==0: core = [i for i in range(1, n+1)]
  elif a==b:
    for i in range(a+b+2):
      if not i%2: core.append(i//2+1)
      else: core.append((a+b+2)//2+i//2+1)
    for i in range(n-a-b-2):
      core.append(i+(a+b+2)+1)
  
  elif a>b:
    for i in range(a+b+2):
      if not i%2: core.append(i//2+1)
      else: core.append((a+b+2)//2+(i+1)//2+1)
    for i in range(a+b+2):
      core[i] += n-a-b-2
    for i in range(n-a-b-2):
      core.append(n-a-b-2-i)
  
  elif a<b:
    for i in range(a+b+2):
      if not i%2: core.append((a+b+2)//2 + i//2 + 1)
      else: core.append(i//2+1)
    for i in range(n-a-b-2):
      core.append(i+(a+b+2)+1)
  

  print(" ".join(list(map(str, core))))
