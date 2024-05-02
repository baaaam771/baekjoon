n, r, c = map(int, input().split())

def find_std(n, x, y):
    length = 2 ** n
    x_start = 0
    x_end = length - 1
    y_start = 0
    y_end = length - 1
    temp = 0
    x_std = (x_end - x_start) // 2
    # print(x_std)
    y_std = (y_end - y_start) // 2
    # print(y_std)
    while length != 1:
        plus = length ** 2 / 4            
        if x <= x_std and y <= y_std:
            x_end = x_std
            y_end = y_std     
        elif x <= x_std and y > y_std:
            temp += plus
            x_end = x_std
            y_start = y_std + 1  
        elif x > x_std and y <= y_std:
            temp += plus * 2
            x_start = x_std + 1
            y_end = y_std  
        elif x > x_std and y > y_std:
            temp += plus * 3
            x_start = x_std + 1
            y_start = y_std + 1 
        # print(temp)
        # print(x_start, x_end)
        # print(y_start, y_end)
        length /= 2
        x_std = x_start + (x_end - x_start) // 2
        # print(x_std)
        y_std = y_start + (y_end - y_start) // 2
        # print(y_std)
    return temp

print(int(find_std(n, r, c)))
