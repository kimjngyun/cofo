import sys
input=sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  arr = list(map(int, input().split()))
  s = input()
  like = []
  dislike = []
  for i in range(n):
    if s[i]=='1': like.append(arr[i])
    else: dislike.append(arr[i])

  dislike.sort(); like.sort()
  dic_dislike = {dislike[i]: i for i in range(len(dislike))}
  dic_like = {like[i]: i for i in range(len(like))}

  for i in range(n):
    if s[i]=='0': print(dic_dislike[arr[i]]+1, end=' ')
    else: print(dic_like[arr[i]]+len(dic_dislike)+1, end=' ')
  print()
