import sys
input=sys.stdin.readline

primes = [2, 3]
p = [0] * 1000001
p[1] = 1; p[2] = 1 ; p[3] = 1
for cand in range(5, 1000001, 2):
  flag = False
  for prime in primes:
    if prime**2 > cand:
      break
    if cand % prime == 0:
      flag = True
      break
  if not flag:
    primes.append(cand)
    p[cand] = 1

def one_or_prime(n):
  if p[n]: return n
  else: return 0

for _ in range(int(input())):
  n, e = map(int,input().split())
  l = list(map(int, input().split()))
  l = list(map(one_or_prime, l))

  ans = 0
  for i in range(0, e):
    t = i
    temp = []
    while t<n:
      temp.append(l[t])
      t+=e
    a, b, c = 0, 0, 0
    for i in range(len(temp)):
      if temp[i]==0: ans += (a*b+a+b)*c; a, b, c = 0, 0, 0
      elif temp[i]==1 and c==0: a+=1
      elif temp[i]==1 and c==1: b+=1
      elif temp[i]>1 and c==0: c=1
      elif temp[i]>1 and c==1: ans += a*b+a+b; a, b, c = b, 0, 1

      if i==len(temp)-1: ans += (a*b+a+b)*c
  print(ans)
