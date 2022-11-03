def prime(a):
    is_prime = True
    for i in range(2,int(a**0.5)+1):
        if a%i == 0:
            is_prime = False
    return is_prime
def palindrome(b):
    rev = 0
    while b:
        rev = rev*10 + b%10
        b = b // 10
    return rev
n = int(input())
for i in range(n+1,n**10):
    if prime(i) == True and palindrome(i)==i:
        print(i)
        break