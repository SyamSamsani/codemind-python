n = int(input())
sq = n*n
temp = n
x = 0
while sq!= 0:
    x += sq%10
    sq = sq//10
if x == temp:
    print('Neon Number')
else:
    print('Not Neon Number')