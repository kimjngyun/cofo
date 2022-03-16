from collections import defaultdict
for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  d = defaultdict(int)

  for i in range(n):
    d[l[i]] += 1

  arr = []
  s = 0
  for i, v in d.items():
    s += 1
    arr.append(v)

  arr.sort(reverse=True)
  ans = len(arr)
  for i in range(n):
    if i < ans: 
      print(ans, end=' ')  
    else:
      print(ans+1, end=' ')
      ans+=1
  print()