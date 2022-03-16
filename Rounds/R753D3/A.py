import sys
input = sys.stdin.readline
t = int(input())  
for _ in range(t):
  a = input().rstrip()
  def idx(c):
    for i in range(0, 26):
      if a[i] == c: return i
  b = input().rstrip()
  ans = 0
  first = idx(b[0])
  if len(b)==1:
    print(0)
  else: 
    for i in range(1, len(b)):
      ans += abs(idx(b[i-1])-idx(b[i]))
    print(ans)
  