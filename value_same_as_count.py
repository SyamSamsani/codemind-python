n = int(input())
lst = list(map(int,input().split()))
l = []
for i in lst:
    if lst.count(i)==i:
        if i in l:
            pass
        else:
            l.append(i)
print(len(l))