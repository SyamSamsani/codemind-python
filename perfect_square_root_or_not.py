n = int(input())
flag = 0
for i in range(1,int(n**0.5)+1):
    if n//i == i and n%i == 0:
        flag = 1
        break
    else:
        flag = 0
if flag == 1:
    print("True")
else:
    print("False")