word = list(input())
reverse = [word[len(word)-i-1] for i in range(len(word))] 
print(1 if word == reverse else 0)