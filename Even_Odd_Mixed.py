n = int(input())
length = s = even = odd = 0
while n!= 0:
    s = n%10
    length += 1
    if s%2==0:
        even += 1
    else:
        odd += 1
    n = n // 10
if length == even:
    print("Even")
elif length == odd:
    print("Odd")
else:
    print('Mixed')
        