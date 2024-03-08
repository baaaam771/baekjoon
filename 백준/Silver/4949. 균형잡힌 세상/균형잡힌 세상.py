mark = ('(', ')', '[', ']')
while 1:
    stk = []
    word = input()
    if word == '.':
        break
    arr = list(word)
    for i in arr:
        if i in mark:
            if len(stk) == 0:
                stk.append(i)
                # print(stk)
            elif i == ')' and stk[-1] == '(':
                stk.pop()
                # print(stk)
            elif i == ']' and stk[-1] == '[':
                stk.pop()
                # print(stk)
            else:
                stk.append(i)
                # print(stk)

    # print(len(stk))
    print('yes' if len(stk)== 0 else 'no')