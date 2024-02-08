list = []
for i in range(int(input())):
    word = input()
    if word not in list:
        list.append(word)
list.sort()


for i in range(1,51):
    for word in list:
        if len(word) == i:
            print(word)
