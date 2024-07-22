def generate_palindromes(n):
    palindromes = []
    length = len(str(n))
    
    for l in range(1, length + 1):
        start = 10 ** ((l - 1) // 2)
        end = 10 ** ((l + 1) // 2)
        for i in range(start, end):
            if l % 2 == 0:
                pal = int(str(i) + str(i)[::-1])
            else:
                pal = int(str(i) + str(i)[-2::-1])
            if pal > n:
                return palindromes
            palindromes.append(pal)
    return palindromes

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    palindromes = generate_palindromes(n)
    print(len(palindromes))
