h,sf,sp = map(int,input().split())
if h>50 and sf>60 and sp>100:
    print(10)
elif h>50 and sf>60:
    print(9)
elif sf>60 and sp>100:
    print(8)
elif h>50 and sp>100:
    print(7)
elif h>50 or sf>60 or sp>100:
    print(6)
else:
    print(5)