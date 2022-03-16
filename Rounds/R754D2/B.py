from collections import deque
import sys
input=sys.stdin.readline

for _ in range(int(input())):
  n = int(input())
  b = list(input().rstrip())
  ans = sorted(b)

  if b == ans: print(0)
  else:
    c = 0
    first = []
    second = []
    for i in range(len(b)):
      if b[i] == '0': c+=1
    c = min(c, len(b)-c)
    for i in range(len(b)):
      if len(first)==c: break
      if b[i]=='1': first.append(i+1)
    for i in range(len(b)):
      if len(second)==c: break
      if b[len(b)-1-i]=='0': second.append(len(b)-i)
    print(1)
    ans = []
    i = 0
    while i<c:
      if first[i]>=second[i]: break
      else: i+=1
    ans = first[:i] + second[:i]
    ans.sort()
    print(len(ans), " ".join(list(map(str, ans))))
