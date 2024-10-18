n = int(input())
word = list(input())
# for i in range(n // 2):
for i in range(n):
    if word[i] == '?':
        if word[-(i+1)] == '?':
            word[i] = 'a'
            word[-(i+1)] = 'a'
        else:
            word[i] = word[-(i+1)]
        
print(''.join(word))