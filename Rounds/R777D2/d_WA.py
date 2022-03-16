import math
def prime(x):
  for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True

for _ in range(int(input())):
  x, d = map(int,input().split())
  cnt = 0
  div = 1
  while x%(d**div)==0:
    div+=1
  div -= 1
  alpha = x//(d**div)

  if not prime(alpha): print("YES"); continue;
  else:
    if div == 2: print("NO")
    else:
      if prime(d): print("NO")
      elif alpha==1: print("YES")
      else:
        root = int(math.sqrt(d))
        if d == root**2 and prime(root): print("NO")
        else: print("YES")
        

      

      

