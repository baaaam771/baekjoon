def daj_ime(x):
    imena = [
        "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen",
        "nineteen"
    ]

    desetice = [
        "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"
    ]

    stotice = [
        "onehundred", "twohundred", "threehundred",
        "fourhundred", "fivehundred", "sixhundred",
        "sevenhundred", "eighthundred", "ninehundred"
    ]

    if x == 0:
        return ""
    if x < 20:
        return imena[x - 1]
    if x < 100:
        return desetice[x // 10 - 2] + daj_ime(x % 10)
    return stotice[x // 100 - 1] + daj_ime(x % 100)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    oblik = data[1:]
    assert len(oblik) == N

    len_sum = sum(len(word) for word in oblik) - 1

    for ans in range(1, 1000):
        if len(daj_ime(ans)) + len_sum == ans:
            break

    assert ans != 1000

    result = []
    for word in oblik:
        if word == "$":
            result.append(daj_ime(ans))
        else:
            result.append(word)
    
    print(' '.join(result))

if __name__ == "__main__":
    main()
