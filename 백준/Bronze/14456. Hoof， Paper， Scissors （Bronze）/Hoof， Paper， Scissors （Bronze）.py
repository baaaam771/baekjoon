import sys
input = sys.stdin.read

def main():
    input_data = input().split()
    N = int(input_data[0])
    cnt1 = 0
    cnt2 = 0
    index = 1

    for _ in range(N):
        a = int(input_data[index])
        b = int(input_data[index + 1])
        index += 2

        if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
            cnt1 += 1
        elif (a == 1 and b == 3) or (a == 3 and b == 2) or (a == 2 and b == 1):
            cnt2 += 1

    print(max(cnt1, cnt2))

if __name__ == "__main__":
    main()