import math

n, m = map(int, input().split())
def combi(n, m):
    return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))

print(combi(n, m))
