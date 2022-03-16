n, d = map(int,input().split())

parent = [0] * (n+1)
for i in range(n+1):
  parent[i] = i

children = [1] * (n+1)
def find(a):
  if a == parent[a]:
    return a
  p = find(parent[a])
  parent[a] = p
  return parent[a]

def union(a,b):
  a = find(a)
  b = find(b)
  if a==b: return
  if a < b: parent[b] = a
  else: parent[a] = b


m = 0
c = 1
for _ in range(d):
  a, b = map(int,input().split())
  if find(a) != find(b):
    t = children[find(a)] + children[find(b)]
    children[find(a)] = t
    children[find(b)] = t
    union(a, b)
  else:
    c+=1
  v = [0] * (n+1)
  s = []
  for i in range(1, n+1):
    if v[find(i)] == 0: s.append(children[find(i)]); v[find(i)]=1
  s.sort(reverse=True)
  ans = 0
  for i in range(c):
    ans+=s[i]
  
  print(ans-1)


    
