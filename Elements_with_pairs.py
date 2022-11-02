n = int(input())
lst = list(map(int,input().split()))
def fun():
    for i in lst:
        print(i,end=' ')
if n%2==0:
    fun()
else:
    fun()
    print('0')