n = int(input())
lst = list(map(int,input().split()))
k = int(input())
l = []
for i in lst:
    if lst.count(i)==k:
        if i in l:
            pass
        else:
            l.append(i)
if len(l)==0:
    print(-1)
else:
    for i in l:
        print(i,end=' ')