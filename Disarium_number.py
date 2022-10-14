n = int(input())
temp = n
rev = init =  0
while n!= 0:
    rev = rev * 10 + n%10
    n = n // 10
i = 0
while rev!= 0:
    i += 1
    init = init + ((rev%10)**(i))
    rev = rev // 10
if temp == init:
    print('True')
else:
    print('False')