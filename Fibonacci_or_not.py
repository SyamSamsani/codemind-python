n = int(input())
a,b = 0,1
if n ==0 or n == 1:
    print('True')
c = a+b
while c<n:
    c = a+b
    a=b
    b=c
if n==c:
    print('True')
else:
    print('False')
    