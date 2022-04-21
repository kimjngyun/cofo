for _ in range(int(input())):
  a, b = map(int,input().split())
  if a==1 or b==1:
    if max(a, b)>2: print(-1)
    else: print(max(a,b)-1)
  else:
    ans = min(a-1, b-1)*2
    t = abs(a-b)
    if t%2==0: ans += t*2
    else: ans += t*2-1
    print(ans)
  