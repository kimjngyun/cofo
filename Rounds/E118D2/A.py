for _ in range(int(input())):
  x1, p1 = map(int,input().split())
  x2, p2 = map(int,input().split())
  while x1>1:
    x1/=10
    p1+=1
  while x2>1:
    x2/=10
    p2+=1
  if p1>p2: print(">")
  if p1==p2:
    if x1>x2: print(">")
    if x1==x2: print("=")
    if x1<x2: print("<")
  if p1<p2: print("<")
