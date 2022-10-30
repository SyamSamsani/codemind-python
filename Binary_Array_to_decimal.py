n = int(input())
lst = list(map(int,input().split()))
lst.reverse()
p = 0
for i in range(len(lst)):
    if lst[i] == 1:
        p = p + 2**i
print(p)