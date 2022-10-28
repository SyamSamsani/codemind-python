n = int(input())
lst = list(map(int,input().split()))
s = 0
for i in range(len(lst)):
    if i%2==1:
        s += lst[i]
print(s)