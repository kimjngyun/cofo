import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a==0 and b==0 and c==1:
        print(3)
    elif a==0 and b==1 and c==0:
        print(2)
    elif a==1 and b==0 and c==1:
        print(2)
    else:
        print((a+2*b+3*c)%2)
         