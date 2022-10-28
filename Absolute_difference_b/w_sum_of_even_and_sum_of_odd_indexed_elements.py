n = int(input())
lst = list(map(int,input().split()))
se = so = 0
for i in range(len(lst)):
    if i%2==0:
        se += lst[i]
    else:
        so += lst[i]
if se>=so:
    print(se-so)
else:
    print(so-se)