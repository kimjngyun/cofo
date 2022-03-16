import sys
input=sys.stdin.readline
def gcd(a, b):
  if b==0: return a
  if a>b: a, b = b, a
  b%=a; 
  return gcd(a, b)
  
for _ in range(int(input())):
  n = int(input())
  arr = list(map(int,input().split()))
  gcd_odd = arr[0]
  gcd_even = arr[1]
  flag = True
  for i in range(0, n, 2):
    gcd_odd = gcd(gcd_odd, arr[i])

  for i in range(1, n, 2):
    if arr[i]%gcd_odd==0: flag = False; break
  if flag: print(gcd_odd); continue

  for i in range(1, n, 2):
    gcd_even = gcd(gcd_even, arr[i])
  
  for i in range(0, n, 2):
    if arr[i]%gcd_even==0: flag = True; break
  if not flag: print(gcd_even); continue

  if flag: print(0)
