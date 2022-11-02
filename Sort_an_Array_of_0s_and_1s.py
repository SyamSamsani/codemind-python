n = int(input())
lst = list(map(int,input().split()))
l = []
for i in lst:
    if i == 0:
        l.append(i)
for j in lst:
    if j == 1:
        l.append(j)
for i in l:
    print(i,end=' ')