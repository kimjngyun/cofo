for _ in range(int(input())):
  n = int(input())
  b = list(map(int, input().split()))
  p = list(map(int, input().split()))
  
  ans = [0] * n
  tree = [[i, 0, 0] for i in range(n+1)]
  root = 0 
  for i in range(n):
    if i+1 == b[i]: root = i+1; continue
    tree[i+1][1] = b[i]
  
  v = [0] * (n+1)
  v[0] = 1
  m = 0
  flag = True
  for i in range(n):
    vertex = p[i]
    parent = tree[vertex][1]
    if v[parent]==0: flag = False; break
    else:
      v[vertex] = 1
      if vertex==root: ans[vertex-1] = m
      else: 
        ans[vertex-1] = m+1-tree[parent][2]
        tree[vertex][2] = m+1
        m = m+1

  if flag:
    for e in ans:
      print(e, end=' ')
    print()
  else: print(-1)
