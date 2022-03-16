import sys
input = sys.stdin.readline
t = int(input())
 
for _ in range(t):
  a, b, c = map(int, input().split()) 
  m = max(a, b, c)
  if(a==m and (b==m or c==m)): print(1, end=' ')
  elif(a==m): print(0, end=' ')
  elif a<m: print(m-a+1, end=' ')
 
  if(b==m and (a==m or c==m)): print(1, end=' ')
  elif(b==m): print(0, end=' ')
  elif b<m: print(m-b+1, end=' ')
 
  if(c==m and (b==m or a==m)): print(1, end=' ')
  elif(c==m): print(0, end=' ')
  elif c<m: print(m-c+1, end=' ')
  print()