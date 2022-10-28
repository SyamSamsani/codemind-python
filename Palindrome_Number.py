def pali(n):
    rev = 0
    temp = n
    while n:
        rev = rev*10 + n%10
        n = n // 10
    return temp == rev
t = int(input())
for i in range(t):
    n = int(input())
    print(pali(n))