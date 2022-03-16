import sys
input=sys.stdin.readline
for _ in range(int(input())):
  w, h = map(int,input().split())
  b = list(map(int, input().split()))
  t = list(map(int, input().split()))
  l = list(map(int, input().split()))
  r = list(map(int, input().split()))
  print(max((b[-1]-b[1])*h, (t[-1]-t[1])*h, (l[-1]-l[1])*w, (r[-1]-r[1])*w))