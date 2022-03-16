for _ in range(int(input())):
  l = [list(map(int, input().split())) for _ in range(3)]
  l.sort(key=lambda x: x[1])
  if l[1][1] == l[2][1]: print(abs(l[1][0]-l[2][0]))
  else: print(0)

