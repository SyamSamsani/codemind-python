n = int(input())
if n<3:
    print("The pattern is not possible")
else:
    for i in range(0,n):
        for j in range(0,i+1):
            print('*',end="")
        print()
    for i in range(n-1,0,-1):
        for j in range(i,0,-1):
            print('*',end='')
        print()