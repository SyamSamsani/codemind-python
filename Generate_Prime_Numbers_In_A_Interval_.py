def prime(n):
    is_prime = True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            is_prime = False
            break
    return is_prime
a = int(input())
b = int(input())
for i in range(a,b+1):
    if prime(i)==True:
        if i == 1:
            pass
        else:
            print(i)