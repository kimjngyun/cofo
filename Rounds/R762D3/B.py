import sys
input=sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  print(int((n+0.1)**(1.0/2.0))+int((n+0.1)**(1.0/3.0))-int((n+0.1)**(1.0/6.0)))