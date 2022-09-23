n = int(input())
s = n*n
temp = rev = 0
while n!=0:
    temp = temp*10 + n%10
    n = n // 10
r = temp**2
while r!=0:
    rev = rev*10 + r%10
    r = r // 10
if s == rev:
    print('True')
else:
    print("False")
