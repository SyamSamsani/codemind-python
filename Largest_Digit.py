n = int(input())
s = []
i = 0
while n > 0:
    l = n % 10
    s.append(l)
    n = n // 10
s=sorted(s)
print(s[-1])