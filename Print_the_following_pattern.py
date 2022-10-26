n = int(input())
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if i == j or n+1 == i+j:
            print(i ,end =' ')
        else:
            print('',end=' ')
    print()
