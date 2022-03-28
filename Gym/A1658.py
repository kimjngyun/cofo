for _ in range(int(input())):
  n = int(input())
  s = input()
  cnt = 2; ans = 0
  for i in range(n):
    if s[i] == '1': cnt += 1
    else: ans += max(2-cnt, 0); cnt = 0
  print(ans)