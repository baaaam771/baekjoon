def sum_digits(N, x):
    ans = 0
    while N:
        ans += N % x
        N //= x
    return ans

def main():
    import sys
    input = sys.stdin.read
    N = int(input().strip())
    
    mx = 0
    p = 0
    
    for i in range(2, N + 1):
        SUM = sum_digits(N, i)
        if SUM > mx:
            mx = SUM
            p = i
    
    print(mx, p)

if __name__ == "__main__":
    main()