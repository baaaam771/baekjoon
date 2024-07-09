def count_pairs_with_same_quotient(n, d, numbers):
    quotient_count = {}
    
    for num in numbers:
        quotient = num // d
        if quotient in quotient_count:
            quotient_count[quotient] += 1
        else:
            quotient_count[quotient] = 1
    
    pair_count = 0
    for count in quotient_count.values():
        if count > 1:
            pair_count += (count * (count - 1)) // 2
    
    return pair_count

n, d = map(int, input().split())
numbers = list(map(int, input().split()))

print(count_pairs_with_same_quotient(n, d, numbers))
