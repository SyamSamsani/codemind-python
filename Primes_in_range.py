def prime(n):
    is_prime = True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            is_prime = False
            break
    return is_prime 
a = int(input())
b = int(input())
count = 0
for i in range(a,b+1):
    if prime(i) == True:
        if i == 1 or i == 0:
            count += 0
        else:
            count += 1
print(count)