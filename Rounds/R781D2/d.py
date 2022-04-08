# UPSOLVED
import sys
input = lambda: sys.stdin.readline().rstrip()

def query(a, b):
  print("?", a, b, flush=True)
  return int(input())

def answer(a):
  print("!", a, flush=True)

for _ in range(int(input())):
  m = 0
  for i in range(30):
    if query(m+1, m+1+(1<<(i+1))) != 1<<(i+1):
      m += 1<<i
  answer((1<<30)-m-1)