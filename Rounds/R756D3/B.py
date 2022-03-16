for _ in range(int(input())):
  a, b = map(int,input().split())
  if a>b: a,b = b,a
  x = (b-a)//2
  y = (a-x)//2
  if b/3>a: print(a)
  else: print(x+y)