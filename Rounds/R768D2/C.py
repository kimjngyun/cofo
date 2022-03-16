for _ in range(int(input())):
  n, k = map(int,input().split())
  if k !=n-1:
    for i in range(n//2):
      if i==0:
        print(k, n-1)
      elif i==k or n-i-1==k:
        print(0, n-1-k)
      elif i!=k:
        print(i, n-i-1)

  else:
    if n==4:
      print(-1)
    else:
      for i in range(n//2):
        if i==0:
          print(n-1, n-2)
        elif i==1:
          print(1, n-3)
        elif i==2:
          print(2, 0)
        else:
          print(i, n-i-1)


