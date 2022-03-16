import sys
input=sys.stdin.readline
MOD = 10**9+7
def extend_euc(a, b):
  if b == 0:
    return a, 1, 0
  gcd, x, y = extend_euc(b, a%b)
  return gcd, y, x-(a//b)*y

def mod_inverse(a, mod):
  g, a, b = extend_euc(a, mod)
  if g > 1: return -1
  return (a + mod) % mod

for _ in range(int(input())):
  n, m, rb, cb, rd, cd, p = map(int,input().split())
  ro, co = rb, cb
  cycle = 0
  maybe = []
  dx, dy = 1, 1
  
  while True:
    if rb+dx==0 or rb+dx==n+1: dx = -dx
    if cb+dy==0 or cb+dy==m+1: dy = -dy
    rb += dx
    cb += dy
    cycle+=1
    if rb == rd or cb == cd: maybe.append(cycle)
    if rb == ro and cb == co: break

  print("c, m", cycle, maybe)
