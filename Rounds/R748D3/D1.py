import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def gcd(x, y):
  if y==0: return x
  else: return gcd(y,x%y)

input = sys.stdin.readline
t = int(input())

for _ in range(t):
  n = int(input())  
  s = set(list(map(int, input().split())))
  sl = list(s)
  sl.sort()
  t = sl[0]
  for i in range(len(sl)):
    sl[i] -= t
  if(len(sl)==1): ans=-1
  elif(len(sl)==2): ans= sl[1]
  else:
    ans = sl[1]
    for i in range(2, len(sl)):
      ans = gcd(ans, sl[i])

  print(ans)