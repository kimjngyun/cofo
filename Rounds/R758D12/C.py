import sys
from math import ceil, log2
input=sys.stdin.readline

class nxSeg():
  def __init__(self, n):
    h = ceil(log2(n))
    t_size = 1 << (h+1)
    self.tree = [0] * t_size

  def set_arr(self, arr):
    self.arr = arr

  def init(self, node, start, end):
    if start == end:
      self.tree[node] = self.arr[start][1]
      return self.tree[node]
    mid = (start + end) // 2
    self.tree[node] = min(self.init(node*2, start, mid), self.init(node*2+1, mid+1, end))
    return self.tree[node]

  def query(self, node, start, end, left, right):
    if start > right or end < left:
      return 10**9+1
    if left <= start and end <= right:
      return self.tree[node]
    mid = (start + end) // 2
    return min(self.query(node*2, start, mid, left, right), self.query(node*2+1, mid+1, end, left, right))
  
  def _min(self, l, r):
    return self.query(1, 0, n-1, l, r)[0]

  def _max(self, l, r):
    return self.query(1, 0, n-1, l, r)[1]


for _ in range(int(input())):
  n = int(input())
  minSeg = nSeg(n)
  maxSeg = xSeg(n)
  ans = [0] * n
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  s = [[0, 0, 0] for _ in range(n)]
  for i in range(n):
    s[i] = [a[i], b[i], i]
  s.sort(key=lambda x: (x[0], x[1]))

  minSeg.set_arr(s)
  minSeg.init(1, 0, n-1)
  maxSeg.set_arr(s)
  maxSeg.init(1, 0, n-1)

  if n>1:
    if minSeg._min(1, n-1)>s[0][1]: ans[s[0][2]] = "0"
    else: ans[s[0][2]] = "1"
    for i in range(1, n-1):
      if minSeg._min(i+1, n-1)>maxSeg._max(0, i-1): ans[s[i][2]] = "0"
      else: ans[s[i][2]] = "1"
  ans[s[n-1][2]] = "1"
  print("".join(ans))

