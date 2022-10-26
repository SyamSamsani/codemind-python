x = int(input())
flag = x
temp = 0
while x:
    n = x%10
    p = 1
    for i in range(1,n+1):
        p *= i
    temp += p
    x = x // 10
if flag == temp:
    print('The number',flag,'is a strong number')
else:
    print('The number',flag,'is not a strong number')