n = int(input())
lst = list(map(int,input().split()))
s = set(lst)
count = 0
for i in s:
    if i%2==0:
        count += 1
print(count)