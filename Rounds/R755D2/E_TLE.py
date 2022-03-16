import sys
input=sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  psum_odd = [0] * (n+1)
  psum_even = [0] * (n+1)
  for i in range(1, n+1):
    if i%2: 
      psum_odd[i] = psum_odd[i-1] + l[i-1]
      psum_even[i] = psum_even[i-1]
    else:
      psum_odd[i] = psum_odd[i-1]
      psum_even[i] = psum_even[i-1] + l[i-1]

  cnt = 0

  for i in range(n):
    for j in range(i, n):
      if i==j:
        if l[i]==0: cnt += 1
      else:
        if l[i]>l[i+1]: break
        if l[j]>l[j-1]: continue
        if psum_odd[j+1]-psum_odd[i] == psum_even[j+1]-psum_even[i]: cnt += 1

  print(cnt)