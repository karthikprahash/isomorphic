# isomorphic
n,m=input().split()
if len(n)==len(m):
    c=0
    d=0
    
    for i in n:
        if i==n[0]:
            c+=1
    
    for j in m:
        if j==m[0]:
            d+=1
if c==d:
    print('yes')
else:
    print('no')
