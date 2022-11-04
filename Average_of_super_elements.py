n = int(input())
lst = list(map(int,input().split()))
l = []
for i in lst:
    if lst.count(i)==i:
        if i in l:
            pass
        else:
            l.append(i)
if len(l)>0:
    avg = sum(l)/len(l)
    print(format(avg,'.2f'))
else:
    print('-1')
        
