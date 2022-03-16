MOD = 998244353
f = [0] * (6001)
invf = [0] * (6001)
f[0], f[1] = 1, 1

for i in range(2, 6001):
  f[i] = f[i-1] * i % MOD

invf[6000] = pow(f[6000], MOD-2, MOD)
for i in range(6000, 0, -1):
  invf[i-1] = (invf[i] * i)% MOD

def ncr(n, r):
  ret = f[n]
  ret *= invf[r]
  ret %= MOD
  ret *= invf[n-r]
  ret %= MOD
  return ret

n, k = map(int,input().split())
s = input()

arr = []
possible = []
dup = []
for i in range(n):
  if s[i]=='1': arr.append(i)

ans = 0

if len(arr)>=k:
  if len(arr)==k:
    possible.append([0, n-1])
  else:
    for i in range(len(arr)-k+1):
      if i==0:
        possible.append([0, arr[k+i]-1])
      elif i==len(arr)-k:
        possible.append([arr[i-1]+1, n-1])
      else: possible.append([arr[i-1]+1, arr[k+i]-1])

  for i in range(len(possible)):
    s, e = possible[i][0], possible[i][1]
    ans += ncr(e-s+1, k)

p = k+1
if len(arr)>=p:
  for i in range(len(arr)-p+1):
    dup.append([arr[i], arr[p+i-1]])

  for i in range(len(dup)):
    s, e = dup[i][0], dup[i][1]
    ans -= ncr(e-s-1, k-1)

if len(possible)==0: print(1)
else:
  print(ans%MOD)