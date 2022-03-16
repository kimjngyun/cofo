import sys
input = sys.stdin.readline
def extend_euc(a, b):
  if b == 0:
    return a, 1, 0
  gcd, x, y = extend_euc(b, a%b)
  return gcd, y, x-(a//b)*y

for i in range(2, 10000):
  x, y = 1212, 5004
  if i%x == y%i: 
    print(i)
    print(extend_euc(x,y))
    print(extend_euc(x, y)[2]+x//extend_euc(x, y)[0])


t= int(input())
for _ in range(t):
  x, y = map(int, input().split())
  if x>y: print(x+y)
  else: print((x+y)//2)

  