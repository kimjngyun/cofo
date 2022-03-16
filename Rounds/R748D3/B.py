import sys
input = sys.stdin.readline

t = int(input())  
for _ in range(t):
  k = int(input())
  t = k
  cnt0 = 0
  while t:
    if(t%10!=0):
      cnt0+=1
    else:
      t//=10
      break
    t//=10
  while t:
    if(t%5!=0):
      cnt0+=1
    else:
      break
    t//=10
  
  t = k
  cnt1 = 0
  while t: 
    if(t%10!=5):
      cnt1+=1
    else:
      t//=10
      break
    t//=10
  while t:
    if(t%5!=2):
      cnt1+=1
    else:
      break
    t//=10
  print(min(cnt0, cnt1))