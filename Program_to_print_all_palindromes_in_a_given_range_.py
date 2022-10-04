a = int(input())
b = int(input())
rev = 0
for i in range(a,b+1):
    temp = i
    while i!=0:
        rev = rev *10 + i%10
        i = i // 10
    if temp == rev :
        print(temp,end = ' ')
    temp = 0
    rev = 0
