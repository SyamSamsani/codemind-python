n = int(input())
lst = list(map(int,input().split()))
t = int(input())
flag = 0
for i in lst:
    if i == t:
        flag += 1
print(flag)