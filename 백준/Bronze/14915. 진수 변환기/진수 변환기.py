def decimal_to_base(m, n):
    if m == 0:
        return '0'
    
    digits = "0123456789ABCDEF"
    result = ''
    
    while m > 0:
        result = digits[m % n] + result
        m = m // n
    
    return result

m, n = map(int, input().split())

print(decimal_to_base(m, n))
