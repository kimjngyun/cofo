import sys
input = sys.stdin.readline
def init_prime(n):
  global prime
  prime = [False,False] + [True]*(n-1)
  for i in range(2,n+1):
    if prime[i]:
      for j in range(2*i, n+1, i):
        prime[j] = False
pl = []
init_prime(100001)
for i in range(100001):
  if prime[i]: pl.append(i)

def check(t, i):
  c = False
  for j in range(2, 3+i):
    if t%j:
      c = True
      break
  return c

t = int(input())
for _ in range(t):
  n = int(input())
  l = list(map(int, input().split()))
  flag = True
  for i in range(n):
    if check(l[i], i)==False: 
      print("NO")
      flag = False
      break
  if flag: print("YES")
    
    
