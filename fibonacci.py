n = int(input())
a,b=0,1
print(a,b,end=' ')
for i in range(2,n):
    n1 = a+b
    a = b
    b = n1
    print(n1,end=' ')