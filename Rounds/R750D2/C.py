import sys
input = sys.stdin.readline
INF = 200001

t = int(input())

for _ in range(t):

    n = int(input())
    s = input().rstrip()
    rs = s[::-1]
    b = [[0] * (n) for _ in range(n)]
    d = [[0] * (n) for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for i in range(1, n):
        if s[i]!=s[i-1]: 
            d[i-1][i] = 1
            b[i-1][i] = 1<<(ord(s[i])-97)
        else: 
            d[i-1][i] = 0
    
    for i in range(2, n):
        for j in range(0, n):
            p = j
            t = i+j
            if t>=n or p>=n: 
                continue

            if s[p] == s[t]: 
                d[p][t] = d[p+1][t-1]
                b[p][t] = b[p+1][t-1]
            else:
                l = INF
                r = INF

                if (b[p+1][t] ^ 1<<(ord(s[p])-97)):
                    l = d[p+1][t] + 1

                if (b[p][t-1] ^ 1<<(ord(s[t])-97)):
                    r = d[p][t-1] + 1
                
                if l==INF and r==INF:
                    b[p][t] = (1<<27)-1
                    d[p][t] = INF
                elif l==INF or r<l:
                    d[p][t] = d[p][t-1] + 1
                    b[p][t] = b[p][t-1] | 1<<(ord(s[t])-97)
                elif r==INF or l<r:
                    d[p][t] = d[p+1][t] + 1
                    b[p][t] = b[p+1][t] | 1<<(ord(s[p])-97)
    
    print(d[0][n-1])