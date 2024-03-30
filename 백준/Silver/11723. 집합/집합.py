import sys
input = sys.stdin.readline
S = set()
for i in range(int(input())):
    command = list(input().split())
    if command[0] == 'add':
        S.add(int(command[1]))
        # print(S)
    elif command[0] == 'remove': 
        if int(command[1]) in S:
            S.remove(int(command[1]))
        else:
            pass
    elif command[0] == 'check':
        if int(command[1]) in S:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if int(command[1]) in S:
            S.remove(int(command[1]))
        else:
            S.add(int(command[1]))
    elif command[0] == 'all':
        S = set({1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20})
    else:
        S = set()