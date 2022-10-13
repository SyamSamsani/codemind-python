m = int(input())
n = int(input())
temp1 = m
temp2 = n
sum1 = sum2 = 0
for i in range(1,m//2+1):
    if m%i == 0:
        sum1 += i
for i in range(1,n//2+1):
    if n%i == 0:
        sum2 += i
if sum1==temp2 and sum2 == temp1:
    print("Amicable")
else:
    print("Not Amicable")