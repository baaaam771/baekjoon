import sys  
input = sys.stdin.readline  

T = int(input())  
check = ['A', 'B', 'C', 'D', 'E', 'F']  
for _ in range(T):  
    result = 'Infected!'  
    target = input().strip()  
    temp = []  
    for i in range(len(target)):  
        if not i == 0 and temp[-1] == 'C' and not target[i] == 'C' and len(target) - i >= 2:  
            result = 'Good'  
            break  
        if not temp:  
            temp.append(target[i])  
        else:  
            if not target[i] == temp[-1]:  
                temp.append(target[i])  

    if result == 'Good':  
        print(result)  
        continue  

    if len(temp) > 5:  
        print('Good')  
        continue  

    if not temp[0] in check:  
        print('Good')  
        continue  

    if temp[0] != 'A':  
        temp.pop(0)  

    val = ['A', 'F', 'C']  
    if val != temp[0:3]:  
        result = 'Good'  
    if not temp[-1] in check:  
        result = 'Good'  
    print(result)