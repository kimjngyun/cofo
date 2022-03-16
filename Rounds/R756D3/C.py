from collections import deque
for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  m = max(l)
  def f(l, m):
    t = l
    l = deque(l)
    d = deque([m])
    while l:
      flag = True
      if len(l)==2:
        if l[1]<l[0]: flag = False
      if len(l)==1:
        if flag: d.appendleft(l[0])
        else: d.append(l[0])
        l.pop()
      elif l[0] < l[-1]:
        d.appendleft(l[0])
        l.popleft()
      else:
        d.append(l[-1])
        l.pop()
    d = list(d)
    for e in d:
      print(e, end=' ')
    print()

  if l.index(m) == 0: 
    l.pop(0)
    f(l, m)

  elif l.index(m) == n-1: 
    l.pop()
    f(l, m)


  else: print(-1)

