s = input().strip()
std = input().strip()
std_len = len(std)

stack = []

for char in s:
    stack.append(char)
    if len(stack) >= std_len and ''.join(stack[-std_len:]) == std:
        del stack[-std_len:]

result = ''.join(stack)
print(result if result else 'FRULA')