def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    
    result = 0
    digit = 1
    
    while n:
        result += (n % 7) * digit
        n //= 7
        digit *= 3  # 3진수 형식이므로 한 칸당 3씩 늘어난다(0, 1, 2)
    
    print(result)

if __name__ == "__main__":
    main()
