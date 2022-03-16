t = int(input())
for _ in range(t):
  l = input()
  if len(l) == 1:
    print(l)
  else:
    if l[0] != l[len(l)-1]:
      if l[0] =='a': l ='b' + l[1:]
      else: l='a' + l[1:]
    print(l)
