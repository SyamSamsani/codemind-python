a,b,c = map(int,input().split())
capacity = 2*a*b*c*512
print(capacity//1024,end='')
print('KB')