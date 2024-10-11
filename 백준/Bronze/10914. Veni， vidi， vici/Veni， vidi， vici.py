# a = 97
n = int(input())
code = list(input().split())

ori = []
for i in code:
    arr = list(i)
    if len(arr) % 2 == 1:
        del arr[-1]
    # print(arr)
    temp = []
    for j in range(len(arr)//2):
        y = ord(arr[2*j])-97
        z = ord(arr[2*j+1])-97
        x = (y+z-n) % 26
        temp.append(chr(x+97))
    temp_string = ''.join(temp)
    ori.append(temp_string)

print(' '.join(ori))