import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  n = int(input())
  l = list(map(int, input().rstrip().split()))
  color = input().rstrip()
  Blue = []
  Red = []
  for i in range(n):
    if color[i]=="B":
      Blue.append(l[i])
    else:
      Red.append(l[i])
  Blue.sort()
  Red.sort(reverse=True)

  flag = True
  for i in range(len(Blue)):
    if Blue[i]<i+1: flag = False
  
  for i in range(len(Red)):
    if Red[i]>n-i: flag = False

  if flag: print("YES")
  else: flag: print("NO")
  