books = {}
for i in range(int(input())):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

ans = ''
n = 0
for i in books:
    if books[i] > n:
        n = books[i]
        ans = i
    if books[i] == n:
        ans = min(ans, i)

print(ans)