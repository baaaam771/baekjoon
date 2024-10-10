for _ in range(int(input())):
    command = list(input())
    if len(command) == 7 and len(set(command)) == 2 and (command[0] == command[1] == command[4]) and (command[2] == command[3] == command[5] == command[6]):
        print(1)
    else:    
        print(0)