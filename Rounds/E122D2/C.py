import sys
input=sys.stdin.readline

def _ceil(a, b):
  return (a+b-1)//b

for _ in range(int(input())):
  hc, dc = map(int,input().split())
  hm, dm = map(int,input().split())
  k, w, a = map(int,input().split())
  def f(i):
    if _ceil(hm, (dc+w*i)) <= _ceil((hc+a*(k-i)), dm): return True
    else: return False

  flag = False
  for i in range(k+1):
    if f(i): flag = True; break; 
  

  if flag: print("YES")
  else: print("NO")