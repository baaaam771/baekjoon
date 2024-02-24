import math

n = int(int(input()))
nums = list(map(int, input().split()))
ans = 0

def prime(num):
    if num == 1:
        return False
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            return False
    return True


for i in nums:
    if prime(i)is True:
        ans += 1
    
print(ans)