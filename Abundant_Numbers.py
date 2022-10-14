n = int(input())
flag = 0
for i in range(1,n):
    if n%i == 0:
        flag += i
if flag > n:
    print('True')
else:
    print('False')