import sys
from math import log2, ceil 
input=sys.stdin.readline
class LST:
  def __init__(self, n):
    h = int(ceil(log2(n)))
    t_size = 1 << (h+1)
    self.tree = [0 for _ in range(t_size)]
    self.lazy = [0 for _ in range(t_size)]

  def set_arr(self, arr):
    self.arr = arr
  
  def init(self, node, s, e):
    if s == e:
      self.tree[node] = self.arr[s]
      return self.tree[node]
    else:
      m = (s+e)//2
      self.tree[node] = self.init(node*2, s, m) + self.init(node*2+1, m+1, e)
      return self.tree[node]

  def update_lazy(self, node, s, e):
    if self.lazy[node] != 0:
      self.tree[node] += self.lazy[node] * (e-s+1)
      if s!=e:
        self.lazy[node*2] += self.lazy[node]
        self.lazy[node*2+1] += self.lazy[node]
      self.lazy[node] = 0 
  
  def update_range(self, node, s, e, l, r, v):
    self.update_lazy(node, s, e)
    if l>e or r<s: return
    if l<=s and e<=r:
      self.tree[node] += v * (e-s+1)
      if s!=e:
        self.lazy[node*2] += v
        self.lazy[node*2+1] += v
      return
    m = (s+e)//2
    self.update_range(node*2, s, m, l, r, v)
    self.update_range(node*2+1, m+1, e, l, r, v)
    self.tree[node] = self.tree[node*2] + self.tree[node*2+1]
    return

  def query(self, node, s, e, l, r):
    self.update_lazy(node, s, e)
    if l>e or r<s: return 0
    if l<=s and e<=r: return self.tree[node]
    m = (s+e)//2
    return self.query(node*2, s, m, l, r) + self.query(node*2+1, m+1, e, l, r)

n, k = map(int,input().split())
b = list(map(int, input().split()))

lst = LST(n)
lst.set_arr(list(0 for _ in range(n)))
lst.init(1, 0, n-1)

def add(l, r, t):
  lst.update_range(1, 0, n-1, l-1, r-1, t)
  lst.update_range(1, 0, n-1, r, r, (-r+l-1)*t)
def get(x):
  return lst.query(1, 0, n-1, 0, x-1)

ans = 0
for i in range(n, 0, -1):
  ai = get(i)
  t = ceil((b[i-1]-ai)/min(k, i))
  if t>0:
    add(max(i-k+1,1),i, t)
    ans += t

print(ans)
