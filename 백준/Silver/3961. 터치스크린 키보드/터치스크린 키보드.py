key = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
point_dict = {}

for i in range(3):
    temp = list(key[i])
    for j in range(len(temp)):
        point_dict[temp[j]] = [i, j]

# print(point_dict) 
for i in range(int(input())):
    word_list = []
    std, l = input().split()
    # print(std)
    # print(l)
    std_arr = list(std)
    for j in range(int(l)):
        temp_word = input()
        temp_word_arr = list(temp_word)
        cnt = 0
        for k in range(len(std_arr)):            
            cnt += abs(point_dict[std_arr[k]][0]- point_dict[temp_word_arr[k]][0])
            cnt += abs(point_dict[std_arr[k]][1]- point_dict[temp_word_arr[k]][1])
        word_list.append([temp_word, cnt])
    # print(std_arr)
    # print(word_list)
    word_list.sort(key=lambda x: (x[1], x[0]))
    for i in word_list:
        print(i[0], i[1])