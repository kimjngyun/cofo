import sys
input=sys.stdin.readline
for _ in range(int(input())):
  arr = list(map(int, input().split()))
  arr.sort()
  if arr[0]+arr[1]==arr[2]: print("YES")
  elif arr[1]==arr[2] and arr[0]%2==0: print("YES")
  elif arr[0]==arr[1] and arr[2]%2==0: print("YES")
  else: print("NO")
