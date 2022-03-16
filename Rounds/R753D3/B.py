import sys
import math
input = sys.stdin.readline
t = int(input())  
for _ in range(t):
  z, n = map(int, input().split())
  if z%2==0: 
    if n%4==1: z-=1+(n//4)*4
    if n%4==2: z+=1
    if n%4==3: z+=4+(n//4)*4
  else:
    if n%4==1: z+=1+(n//4)*4
    if n%4==2: z-=1
    if n%4==3: z-=4+(n//4)*4
  print(z)
