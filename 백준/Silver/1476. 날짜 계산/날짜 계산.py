e, s, m = map(int, input().split())

year = e
while True:
    if (year-s) % 28 == 0 and (year-m) % 19 == 0:
        break
    year += 15
print(year)