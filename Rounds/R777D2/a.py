for _ in range(int(input())):
  n = int(input())
  if n%3==0: print("21"*(n//3))
  elif n%3==1: print("12"*(n//3)+"1")
  else: print( "21"*(n//3)+"2")