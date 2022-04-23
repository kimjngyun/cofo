import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  s = input()
  b = s.split('a')
  flag = True
  for bb in b:
    if len(bb)==1: flag = False
  a = s.split('b')
  for aa in a:
    if len(aa)==1: flag = False
  if not flag or len(s)==1: print("NO")
  else: print("YES")