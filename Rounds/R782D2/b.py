for _ in range(int(input())):
  n, k = map(int,input().split())
  odd = True if k%2 else False
  s = list(input())
  s = list(map(int, s))
  ans = [0] * n
  idx = 0
  for i in range(n):
    if odd: 
      if s[i]==1 and k>0: ans[i] = 1; k-=1;
    else:
      if s[i]==0 and k>0: ans[i] = 1; k-=1; 
  ans[-1] += k
  for i in range(n):
    if odd and ans[i]%2==0: s[i] = s[i] ^ 1
    if not odd and ans[i]%2==1: s[i] = s[i] ^ 1
  print("".join(map(str, s)))
  print(*ans)
