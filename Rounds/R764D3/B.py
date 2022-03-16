def solve(a, b, c):
  if (a+c)&1==0 and ((a+c)//2)>=b and((a+c)//2)%b==0: print("YES"); return
  if (2*b-a)>=c and (2*b-a)%c==0: print("YES"); return
  if (2*b-c)>=a and (2*b-c)%a==0: print("YES"); return
  print("NO")


for _ in range(int(input())):
  a, b, c = map(int,input().split())
  solve(a, b, c)