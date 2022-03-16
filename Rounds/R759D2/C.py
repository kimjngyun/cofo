import sys
input=sys.stdin.readline
for _ in range(int(input())):
  n, k = map(int,input().split())
  l = list(map(int, input().split()))
  pos = []
  neg = []
  for i in range(n):
    if l[i]>0: pos.append(l[i])
    elif l[i]<0: neg.append(-l[i])
  pos.sort()
  neg.sort()
  ans = 0
  for i in range(len(pos)-1, -1, -k):
    ans += pos[i]*2
  for i in range(len(neg)-1, -1, -k):
    ans += neg[i]*2
  if len(pos)==0 and len(neg)==0: ans=0
  elif len(pos)==0: ans -= neg[-1]
  elif len(neg)==0: ans -= pos[-1]
  elif neg[-1]>pos[-1]: ans -=neg[-1]
  else: ans -= pos[-1]
  print(ans)



  
