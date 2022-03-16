from collections import deque
def brev(n):
  ret = 0
  s = []
  while n:
    if n&1: s.append(1)
    else: s.append(0)
    n//=2
  for i in range(len(s)):
    ret += 2**(len(s)-1-i)*s[i]
  return ret

def r1(n):
  n = (n<<1)+1
  return brev(n)

def r0(n):
  n = n<<1
  return brev(n)

def c1(n):
  ret = 0
  while n:
    if n&1: ret+=1
    n//=2
  return ret

x, y = map(int,input().split())
c1x = c1(x)
c1y = c1(y)

q = deque([[x, 0]])
visited = set()
flag = True
visited.add(x)
while q:
  curr, step = q.popleft()
  visited.add(curr)
  if curr==y: print("YES"); flag = False; break;
  next0 = r0(curr)
  if next0 not in visited and c1(next0): 
    q.append([next0, step+1])
    visited.add(next0)

  next1 = r1(curr)
  if next1 not in visited and c1(next1)<=c1y: 
    q.append([next1, step+1])
    visited.add(next1)

if flag: print("NO")