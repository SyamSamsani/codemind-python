a = int(input())
b = int(input())
for n in range(a,b+1):
    r = flag=count= 0
    temp = n
    while n:
        r = n%10
        flag += 1
        if r!=0 and temp%r==0:
            count += 1
        else:
            break        
        n = n//10
    if count == flag:
        print(temp,end=' ')
    