import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n = int(input())
  s = list(input().split('W'))

  flag = True
  for seg in s:
    if len(seg)>0 and seg==seg[0]*len(seg): flag=False; break;
  if flag: print("YES")
  else: print("NO")