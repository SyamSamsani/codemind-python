n = int(input())
lst = list(map(int,input().split()))
s= 0
for i in lst:
    if i%2==0:
        break
    else:
        s += i
print(s)