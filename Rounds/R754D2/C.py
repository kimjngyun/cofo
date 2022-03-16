import sys
from typing import AsyncIterable
input=sys.stdin.readline

for _ in range(int(input())):
  n = int(input())
  s = input().rstrip()
  flag = True
  for i in range(n):
    if s[i]=='a':
      if i+1<n and s[i+1]=='a': print(2); flag=False; break
  if flag:
    for i in range(n):
      if s[i]=='a':
        if i+2<n and s[i+2]=='a': print(3); flag=False; break
  if flag:
    for i in range(n):
      if s[i]=='a':
        if i+3<n and s[i+3]=='a'and s[i+1]=='b' and s[i+2]=='c': print(4); flag=False; break
        if i+3<n and s[i+3]=='a'and s[i+1]=='c' and s[i+2]=='b': print(4); flag=False; break
  if flag:
    for i in range(n):
      if s[i]=='a':
        if i+6<n and s[i:i+7]=='abbacca': print(7); flag=False;break
        if i+6<n and s[i:i+7]=='accabba': print(7); flag=False;break
  
  if flag:print(-1)