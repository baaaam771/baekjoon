import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# print(n, m)
book = {input().rstrip():i+1 for i in range(n)}
# print(book)
convert_book = {v:k for k,v in book.items()}

for i in range(m):
    ele = input().rstrip()
    if ele.isdecimal():
        print(convert_book[int(ele)])
    else:
        print(book[ele])
    
