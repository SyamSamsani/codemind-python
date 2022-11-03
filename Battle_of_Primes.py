def prime(a):
    is_prime = True
    for i in range(2,int(a**0.5)+1):
        if a%i == 0:
            is_prime = False
            break
    return is_prime
n1 = int(input())
n2 = int(input())
a = n1+n2
for i in range(1,1000):
    if prime(a+i)==True:
        print(i)
        break
