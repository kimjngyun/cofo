from readline import insert_text
import sys
input=sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  if n%7==0: print(n)
  else:
    n = n - n%10
    for i in range(10):
      if (n+i)%7==0:
        print(n+i)
        break
