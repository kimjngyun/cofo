for _ in range(int(input())):
  l = list(input())
  n = list(map(int, l))
  if n[len(n)-1] %2 == 0: print(0)
  elif n[0] %2 == 0: print(1)
  else:
    flag = True
    for i in range(len(n)):
      if n[i] %2 == 0: print(2); flag=False; break
    if flag: print(-1)