def solve(n, s):
  if n==1 or s=='10' or s=='01': print("YES")
  else: print("NO")


for _ in range(int(input())):
  n = int(input())
  s = input()
  solve(n, s)

