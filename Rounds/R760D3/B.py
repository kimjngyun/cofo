import sys
input=sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  arr = list(input().split())
  flag = True
  s = arr[0]
  for i in range(1, n-2):
    if arr[i][0]== arr[i-1][1]: s+=arr[i][1]
    else: s+=arr[i]; flag = False
  if flag: s+='a'
  print(s)