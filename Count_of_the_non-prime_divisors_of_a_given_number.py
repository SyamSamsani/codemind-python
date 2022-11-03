n = int(input())
l = []
for i in range(1,n+1):
    if n%i == 0:
        l.append(i)
count = 0
def prime(a):
    is_prime = True
    for i in range(2,int(a**0.5)+1):
        if a%i == 0:
            is_prime = False
            break
    return is_prime
for i in l:
    if i == 1:
        count += 1
    if prime(i)==False:
        count += 1
print(count)