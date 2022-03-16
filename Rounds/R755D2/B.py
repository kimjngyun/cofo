for _ in range(int(input())):
  a, b = map(int,input().split())
  if a>b: a, b = b, a
  ans = a//3 * b
  a %= 3
  if a==1:
    if b%3 == 0: ans += b//3
    else: ans += b//3 + 1
  if a==2:
    if b%3 == 0: ans += (b//3)*2
    if b%3 == 1: ans += (b//3)*2 + 1
    if b%3 == 2: ans += (b//3)*2 + 2
  print(ans)