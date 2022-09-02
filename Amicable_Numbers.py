a = int(input())
b = int(input())
s = 0
c = 0
for i in range(1,a):
    if a % i == 0:
        s += i
for i in range(1,b):
    if b % i == 0:
        c += i
if s == b and c == a:
    print("Amicable")
else:
    print("Not Amicable")