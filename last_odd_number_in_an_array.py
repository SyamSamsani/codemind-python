n = int(input())
lst = list(map(int,input().split()))
for i in range(len(lst)-1,-1,-1):
    if lst[i]%2==1:
        print(lst[i])
        break