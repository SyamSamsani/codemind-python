a,b = map(int,input().split())
if a > b:
    max = a
elif b > a:
    max = b
else:
    print(a)
while True:
    if max%a==0 and max%b==0:
        print(max)
        break
    else:
        max += 1