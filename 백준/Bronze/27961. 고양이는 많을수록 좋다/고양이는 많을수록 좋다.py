n = int(input())
if n == 0:
    print(0)
    exit(0)
cat = 0
while 2 ** cat < n:
    cat += 1
print(cat+1)