a, b = map(int, input().split())
temp = a * b // 24200
print(temp+1 if a * b % 24200 >0 else temp)