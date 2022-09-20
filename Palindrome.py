n = int(input())
temp = n
rem = 0
while n > 0:
    rem = rem * 10 + (n%10)
    n = n // 10
if temp == rem:
    print("True")
else:
    print("False")