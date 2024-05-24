for i in range(int(input())):
    oper = list(input())
    num = int(input())
    # t_arr = list(input())
    t_arr = input()
    t_arr = t_arr[1:-1]
    if len(t_arr) == 0:
        arr = []
    else:
        arr = list(map(int, t_arr.split(',')))

    # print(oper)
    # print(arr)
    std = 1
    error = False
    for i in oper:
        if i == 'R':
            std *= -1
        elif i == 'D' and len(arr) == 0:
            print('error')
            error = True
            break
        elif i == 'D' and std == 1:
            arr.pop(0)
        elif i == 'D' and std == -1:
            arr.pop(-1)
    if error == False:
        if std == 1:
            print(str(arr).replace(" ", ""))
        else:
            arr.reverse()
            print(str(arr).replace(" ", ""))
