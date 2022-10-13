n = int(input())
temp = n
sq = n*n
a = b = 0
while n!= 0 and sq!=0:
    a = a*10 + n%10
    b = b*10 + sq%10
    n = n//10
    sq = sq//10
if a == b:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')