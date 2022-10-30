n = int(input())
lst = list(map(int,input().split()))
count = 0
for i in lst:
    if i == 1 or i == 0:
        count += 1
print(len(lst)==count)