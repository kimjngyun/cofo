mod = 998244353
def fac(n, mod):
  ret = 1
  for i in range(1, n+1):
    ret *= i
    ret %= mod
  return ret%mod
for _ in range(int(input())):
  n = int(input())
  if n%2: print(0)
  else: print((fac(n//2, mod)**2)%mod)

