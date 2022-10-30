n = int(input())
lst = list(map(int,input().split()))
avg = sum(lst)//len(lst)
count = 0
for i in lst:
    if i<=avg:
        count += 1
    else:
        count += 0
print(count)