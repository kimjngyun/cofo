import sys
input=sys.stdin.readline
class DisjointSetUnion:
  def __init__(self, n):
    self.parent = list(range(n))
    self.size = [1] * n
    self.num_sets = n
 
  def find(self, a):
    acopy = a
    while a != self.parent[a]:
      a = self.parent[a]
    while acopy != a:
      self.parent[acopy], acopy = a, self.parent[acopy]
    return a
 
  def union(self, a, b):
    a, b = self.find(a), self.find(b)
    if a != b:
      if self.size[a] < self.size[b]:
        a, b = b, a
      self.num_sets -= 1
      self.parent[b] = a
      self.size[a] += self.size[b]
 
  def set_size(self, a):
    return self.size[self.find(a)]
 
  def __len__(self):
    return self.num_sets

MAX = 10**9
MAX_B = MAX.bit_length()
for _ in range(int(input())):
  input()
  n, m = map(int,input().split())
  edge_groups = [[] for _ in range(MAX_B)]
  edges = [[0,0] for _ in range(m)]
  for i in range(m):
    edges[i][0], edges[i][1], w = map(int,input().split())
    for j in range(MAX_B):
      if w & (1<<j):
        edge_groups[j].append(i)
    

  ans = 2**MAX_B - 1 
  remaining = set(range(m))

  for i in reversed(range(MAX_B)):
    removed = set()
    for j, k in enumerate(edge_groups[i]):
      if k in remaining:
        remaining.remove(k)
        removed.add(k)
    
    dsu = DisjointSetUnion(n)
    for j in remaining:
      dsu.union(edges[j][0]-1, edges[j][1]-1)
    
    if len(dsu) == 1: ans ^= 1<<i
    else:
      for i in removed:
        remaining.add(i)
  
  print(ans)