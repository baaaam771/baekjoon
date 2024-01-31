n = int(input())
nogroup = 0
for _ in range(n):
    word = list(input())
    uniq = []
    for i in range(len(word)):
        if word[i] not in uniq:
            uniq.append(word[i])
        else:
            if word[i-1] != word[i]:
                nogroup += 1
                break
            else:
                pass

print(n-nogroup)


