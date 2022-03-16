for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  for i in range(n):
    l[i] = [i+1, l[i]]
  l.sort(key=lambda x: x[1], reverse=True)
  ans = [0] * (n+1)
  ret = 0
  x = 0
  for e in l:
    ni = 0
    if x==0: ni = 1
    elif x>0: ni = -x
    elif x<0: ni = -x + 1
    ans[e[0]] = ni
    ret += 2*abs(ni)*e[1]
    x = ni
  print(ret)
  for e in ans:
    print(e, end=' ')