n = int(input())

m = int(input())
s = input()

arr = []

i = 0
cnt_len = 0
ans = 0
while i < m-1:
    if s[i:i+3] == 'IOI':
        cnt_len += 1
        i += 2
        if cnt_len == n:
            ans += 1
            cnt_len -= 1
    else:
        cnt_len = 0
        i += 1

print(ans) 