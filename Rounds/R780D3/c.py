import sys
sys.setrecursionlimit(10**6)
for _ in range(int(input())):
  st = input()
  # st = 'abcbc' * 40000
  n = len(st)
  dp = [-1] * (n+1)
  dp[n] = 0
  dp[n-1] = 1
  if n>1: dp[n-2] = 0 if st[-1]==st[-2] else 2

  def f(n):
    if dp[n]>-1: return dp[n]
    nxt = st.find(st[n], n+1)
    if nxt == -1:
      dp[n] = f(n+1) + 1
    else:
      dp[n] = min(f(nxt+1)+ nxt-n-1, f(n+1)+1)
    return dp[n]

  for i in range(n,-1,-1):
    f(i)
  print(f(0))
  


