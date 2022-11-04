n = int(input())
lst = list(map(int,input().split()))
l = set(lst)
s = 0
for i in l:
    if i%2==1:
        s += i
print(s)