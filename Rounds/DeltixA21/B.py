import sys
input=sys.stdin.readline
n, q = map(int,input().rstrip().split())
s = list(input().rstrip())
cand = [0] * (n+1)
cnt = 0
for i in range(n-2):
  if s[i:i+3] == ['a','b','c']: cand[i] = 1; cnt+=1

for _ in range(q):
  i, c = input().rstrip().split()
  i = int(i)-1
  s[i] = c
  for j in range(max(0, i-2) , min(i+1, n-2)):
    if s[j:j+3] == ['a', 'b', 'c']:
      if cand[j] == 0: cand[j] = 1; cnt += 1
    else:
      if cand[j] == 1: cand[j] = 0; cnt -= 1
  print(cnt)

