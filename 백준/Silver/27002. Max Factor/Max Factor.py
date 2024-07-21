def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    p = 2
    while (p * p <= max_num):
        if (is_prime[p] == True):
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, max_num + 1) if is_prime[p]]
    return prime_numbers

def largest_prime_factors(max_num, primes):
    largest_prime_factor = [0] * (max_num + 1)
    for prime in primes:
        for multiple in range(prime, max_num + 1, prime):
            largest_prime_factor[multiple] = prime
    return largest_prime_factor

def find_number_with_largest_prime_factor(numbers, largest_prime_factor):
    max_prime_factor = -1
    result_number = -1
    for number in numbers:
        if largest_prime_factor[number] > max_prime_factor:
            max_prime_factor = largest_prime_factor[number]
            result_number = number
    return result_number

# 최대 수와 N을 입력 받음
max_num = 20000
N = int(input())
numbers = [int(input()) for _ in range(N)]

# 에라토스테네스의 체로 소수 구하기
primes = sieve_of_eratosthenes(max_num)

# 각 숫자의 가장 큰 소인수 구하기
largest_prime_factor = largest_prime_factors(max_num, primes)

# 가장 큰 소인수를 가진 숫자 찾기
result = find_number_with_largest_prime_factor(numbers, largest_prime_factor)

print(result)
