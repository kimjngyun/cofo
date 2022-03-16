for _ in range(int(input())):
  n = int(input())
  s = list(input())
  t = 10000
  ans = ''
  for i in range(n):
    if ord(s[i])<t or (i>1 and ord(s[i])==t):
      ans += s[i]
      t = ord(s[i])
    else: break
  ans = list(ans)
  ans += ans[::-1]
  print("".join(ans))

