import sys
input=sys.stdin.readline

for _ in range(int(input())):
  n = int(input())
  for i in range(n):
    print(i+2, end=" ")
  print()