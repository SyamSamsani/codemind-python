n = int(input())
lst = list(map(int,input().split()))
l = []
a = []
for i in lst:
    if i in l:
        pass
    else:
        l.append(i)
        a.append(i)
        s = lst.count(i)
        a.append(s)
for j in a:
    print(j,end=' ')