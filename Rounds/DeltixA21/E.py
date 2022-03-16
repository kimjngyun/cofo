import sys
input=sys.stdin.readline
n, q = map(int,input().rstrip().split())
s = list(input().rstrip())
fa, fb, fc = 0, 0, 0
for i in range(n):
  if s[i]=='a': fa=i
  if s[i]=='b' and fa and not fb: fb=i
  if s[i]=='c' and fb and not fc: fc=i; break
for _ in range(q):
  i, c = input().rstrip().split()
  i = int(i)-1
  s[i] = c


