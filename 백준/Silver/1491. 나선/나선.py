n, m = map(int, input().split())
a = 0
b = 0
if n > m:
    b = m // 2
    if m % 2 == 0:
        a = -1 + b
    else:
        a = n -1 - b
elif n < m:
    a = n // 2
    if n % 2 == 0:
        a -= 1
    if n % 2 == 0:
        b = a + 1
    else:
        b = m - 1 - a 
        
else:
    if n % 2 == 1:
        a, b = n//2, n//2
    else:
        a = n//2 - 1
        b = n//2

print(a, b)