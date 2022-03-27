for _ in range(int(input())):
  n, k = map(int,input().split())
  l = list(map(int, input().split()))
  l = list(set(l))
  l.sort()
  s = 0; e = 1
  flag = False;
  while True:
    if s==e: e+=1;
    elif e>=len(l): break;
    elif l[e]-l[s]==k: flag=True; break;
    elif l[e]-l[s]>k: s+=1;
    elif l[e]-l[s]<k: e+=1;
  if flag: print("YES")
  else: print("NO")
