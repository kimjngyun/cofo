from cmath import inf
import sys
input=sys.stdin.readline
for _ in range(int(input())):
  s = input().rstrip()
  one = 0
  zero = 0

  for i in range(len(s)):
    if s[i]=='1': one += 1
    else: zero += 1
  if one>zero: print(zero)
  elif one<zero: print(one)
  else: print(one-1)