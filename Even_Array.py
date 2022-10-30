n = int(input())
lst = list(map(int,input().split()))
count = 0
for i in lst:
    if i%2==0:
        count += 1
print(len(lst)==count)