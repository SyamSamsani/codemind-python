def palindrome(n):
    s = 0
    while n:
        s = s*10 + n%10
        n = n//10
    return s
n = int(input())
for i in range(n+1,10*n):
    if (i==palindrome(i)):
        fp = i
        break
for i in range(n-1,1,-1):
    if (i==palindrome(i)):
        sp = i
        break
if ((fp-n)>(n-sp)):
    print(sp)
elif ((fp-n)<(n-sp)):
    print(fp)
else:
    print(sp,fp)
    