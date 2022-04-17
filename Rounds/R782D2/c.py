for _ in range(int(input())):
  n, a, b = map(int,input().split())
  x = [0] + list(map(int, input().split()))

  pref = [0] * (n+2)
  for i in range(1, n+2):
    pref[i] = pref[i-1]+x[i-1]

  def _sum(i, j):
    return pref[j]-pref[i-1]
  MIN = 10**30
  for idx in range(0, n):
    MIN = min(MIN, (a+b)*x[idx] -  b*(n-idx)*x[idx] +  b*_sum(idx+2, n+1))
  print(MIN)
