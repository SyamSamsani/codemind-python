n = int(input())
s = 0
p = 1
i = 0
while n > 0:
    s += n % 10
    p *= n % 10
    n = n // 10
print(p-s)