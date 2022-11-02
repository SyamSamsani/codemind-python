n = int(input())
lst = list(map(int,input().split()))
l = []
for i in lst:
    if i in l:
        pass
    else:
        l.append(i)
for j in l:
    print(j,end=' ')