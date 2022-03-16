import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  s = list(input().rstrip())
  idx = 0
  MIN = ord(s[0])
  for i in range(1, len(s)):
    if ord(s[i]) < MIN:
      idx = i
      MIN = ord(s[i])
  print(s[idx], "".join(s[:idx]+s[idx+1:]))
