def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

for i in range(int(input())):
    a, b = map(int, input().split())
    print(a*b // gcd(a, b))