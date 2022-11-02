n = int(input())
lst = list(map(int,input().split()))
a,b = map(int,input().split())
l = []
for i in lst:
    if i<a or i>b:
        l.append(i)
if len(l)>0:
    for i in l:
        print(i,end=' ')
else:
    print('-1')