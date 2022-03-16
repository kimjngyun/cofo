import sys
input=sys.stdin.readline
q = int(input())
ql = [list(map(int,input().split())) for _ in range(q)]
ql.reverse()
ans = []
upd = {}

for i in range(q):
  if ql[i][0] == 1:
    if upd.get(ql[i][1]) != None:
      ans.append(upd[ql[i][1]])
    else: ans.append(ql[i][1])

  if ql[i][0] == 2:
    if upd.get(ql[i][2]) != None:
      upd[ql[i][1]] = upd[ql[i][2]]
    else:
      upd[ql[i][1]] = ql[i][2]
    
ans.reverse()
print(*ans)
