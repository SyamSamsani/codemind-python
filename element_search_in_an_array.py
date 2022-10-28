n = int(input())
lst = list(map(int,input().split()))
t = int(input())
b = False
for i in lst:
    if i == t:
        b = True
        break
print(b)