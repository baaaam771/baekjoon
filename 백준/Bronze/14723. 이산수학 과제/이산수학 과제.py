n = int(input())
num = 0
i = 0
while num < n:
    i += 1
    num += i

sub = num - n
print(1+sub, i-sub)