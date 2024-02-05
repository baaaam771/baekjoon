n=int(input())
for i in range(n):
    list = []
    list.append(' '*(n-i-1))
    list.append('*'*(2*i+1))
    #list.append(' '*(n-i-1))
    print(''.join(list))
for i in range(n-1):
    list = []
    list.append(' '*(i+1))
    list.append('*'*(2*(n-i-1)-1))
    #list.append(' '*(i+1))
    print(''.join(list))
    
