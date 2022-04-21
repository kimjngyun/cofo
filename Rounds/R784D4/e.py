def ncr(n, r):
  ret = 1
  for i in range(r):
    ret *= (n-i)
    ret /= (i+1)
  return int(ret)
import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n = int(input())
  l = [list(input()) for _ in range(n)]
  s = [[0] * 12 for _ in range(12)]
  e = [[0] * 12 for _ in range(12)]
  for i in range(n):
    x = ord(l[i][0]) - ord('a')
    y = ord(l[i][1]) - ord('a')
    s[x][y] += 1
    e[y][x] += 1

  ans = 0
  for i in range(12):
    st = []
    et = []
    for j in range(12):
      if s[i][j]>0: st.append(s[i][j])
      if e[i][j]>0: et.append(e[i][j])
    if len(st)>1: 
      ans += ncr(sum(st), 2)
      for i in range(len(st)):
        if st[i]>1: ans -= ncr(st[i], 2);
    if len(et)>1: 
      ans += ncr(sum(et), 2)
      for i in range(len(et)):
        if et[i]>1: ans -= ncr(et[i], 2)
        
  print(ans)


