def R(num):
    if num == 1:
        return 0
    else:
        return (num-1) // 5 + 1
    
def C(num):
    if num == 1:
        return 0
    else:
        return (num-1) // 7 + 1

def I(num):
    if num == 1:
        return 0
    else:
        return (num-1) // 4 + 1

zone, floor = input().split()
if zone == 'residential':
    print(R(int(floor)))
elif zone == 'commercial':
    print(C(int(floor)))
else:
    print(I(int(floor)))

