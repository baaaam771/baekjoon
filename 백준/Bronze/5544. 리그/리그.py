def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    matches = data[1:]

    arr = [(0, i + 1) for i in range(N)]
    ans = [0] * (N + 1)

    for i in range(0, len(matches), 4):
        A = int(matches[i]) - 1
        B = int(matches[i + 1]) - 1
        C = int(matches[i + 2])
        D = int(matches[i + 3])
        
        if C < D:
            arr[B] = (arr[B][0] + 3, arr[B][1])
        elif C > D:
            arr[A] = (arr[A][0] + 3, arr[A][1])
        else:
            arr[A] = (arr[A][0] + 1, arr[A][1])
            arr[B] = (arr[B][0] + 1, arr[B][1])
    
    arr.sort()

    ans[arr[-1][1]] = 1
    r = 1
    for i in range(N - 2, -1, -1):
        if arr[i][0] != arr[i + 1][0]:
            r = N - i
        ans[arr[i][1]] = r

    for i in range(1, N + 1):
        print(ans[i])

if __name__ == "__main__":
    main()
