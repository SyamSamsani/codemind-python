m = int(input())
if m == 0:
    print("0")
f = 0
s = 1
t = f+s
while t <= m:
    f = s
    s = t
    t = f+s
if abs(t-m) > abs(s-m):
    print(s)
elif abs(t-m) == abs(s-m):
    print(s,t)
else:
    print(t)