n = int(input())
s = 0
while n!= 0 or s>9:
    if (n==0):
        n = s
        s = 0
    r = n%10
    s = s + r**2
    n = n // 10
if s == 1 or s == 7:
    print('True')
else:
    print('False')
    