import sys
input=sys.stdin.readline
for _ in range(int(input())):
  l = list(map(int, input().split()))
  ans = [min(l)]
  s = 1; e = 5
  while s<e:
    if l[0]+l[s]+l[e]==l[6]: print(l[0], l[s], l[e]); break;
    elif l[0]+l[s]+l[e]<l[6]: s+=1
    elif l[0]+l[s]+l[e]>l[6]: e-=1

  