def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        x1 = int(data[index])
        y1 = int(data[index+1])
        x2 = int(data[index+2])
        y2 = int(data[index+3])
        x3 = int(data[index+4])
        y3 = int(data[index+5])
        x4 = int(data[index+6])
        y4 = int(data[index+7])
        index += 8
        
        ans = (x2 - x1) * (y2 - y1) - (max((min(x2, x4) - max(x1, x3)), 0) * max((min(y2, y4) - max(y1, y3)), 0))
        results.append(ans)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
