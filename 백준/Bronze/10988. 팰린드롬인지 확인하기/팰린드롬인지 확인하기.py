word = list(input())
reverse = [word[len(word)-i-1] for i in range(len(word))] 

if word == reverse:
    print(1)
else:
    print(0)