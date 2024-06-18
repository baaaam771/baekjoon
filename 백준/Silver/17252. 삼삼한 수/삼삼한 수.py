def is_three_sum(x):
    if x == 0:
        return "NO"
    
    while x > 0:
        if x % 3 == 2:
            return "NO"
        x //= 3
    
    return "YES"

N = int(input())
print(is_three_sum(N))
