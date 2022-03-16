import sys

input=sys.stdin.readline

for _ in range(int(input())):
  n = int(input())
  arr = list(map(int, input().split()))
  x = int(input())
  pref = [0] * (n+1)
  for i in range(1, n+1):
    pref[i] = pref[i-1]+arr[i-1]
  
  cnt=0
  i = 0
  while i<n-1:
    for j in range(i+1, n):
      if pref[j+1]-pref[i]<x*(j-i+1):
        i = j+1
        cnt+=1
    i+=1

  print(n-cnt)

