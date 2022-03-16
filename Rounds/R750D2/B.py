import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    one, zero = 0, 0
    s = 0 
    for i in range(n):
        if l[i] == 1:
            one += 1
        elif l[i] == 0:
            zero += 1
        s += l[i]
    
    if s == 0:
        print(0)
    else:
        print(one*(2**zero))