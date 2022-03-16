import sys
input = sys.stdin.readline

def extend_euc(a, b):
  if b == 0:
    return a, 1, 0
  gcd, x, y = extend_euc(b, a%b)
  return gcd, y, x-(a//b)*y

t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  bits = [0] * len(list(format(sum(a), 'b')))
  for e in a:
    t = list(format(e, 'b'))
    bl = t[::-1]
    for i in range(len(bl)):
      if bl[i]=='1':
        bits[i] += 1
  gcd = min(bits)
  for e in bits:
    if e: gcd = extend_euc(gcd, e)[0]
  if gcd==0:
    for i in range(1,n+1):
      print(i, end=" ")
  else:
    for i in range(1, gcd+1):
      if gcd%i==0: print(i, end=" ")
  print()