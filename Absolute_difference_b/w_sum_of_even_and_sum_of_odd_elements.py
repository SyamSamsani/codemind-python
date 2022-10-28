n = int(input())
lst = list(map(int,input().split()))
se = so = 0
for i in lst:
    if i%2==0:
        se += i
    else:
        so += i
if se>=so:
    print(se-so)
else:
    print(so-se)