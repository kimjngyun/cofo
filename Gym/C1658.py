for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))

  if l.count(1) != 1: print("NO"); continue;
  l.append(l[0])
  flag = True
  for i in range(n):
    if l[i+1]-l[i] > 1: flag = False; break;
  
  if flag: print("YES")
  else: print("NO")