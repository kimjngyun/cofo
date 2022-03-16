import sys
input=sys.stdin.readline
def gcd(a,b):
  if b==0: return a
  if a>b: a, b = b, a
  b %= a
  return gcd(a, b)

def f(n):
  cnt = 0
  p = 2
  while n>1:
    if n%p==0:
      n//=p
      cnt+=1
    else: p+=1
  return cnt

for _ in range(int(input())):
  a, b, k = map(int,input().split())
  t = f(a) + f(b)
  if k==1: 
    if(a%b==0 or b%a==0) and a!=b: print("YES")
    else: print("NO")
  elif k<=t:
    print("YES")
  else: print("NO")