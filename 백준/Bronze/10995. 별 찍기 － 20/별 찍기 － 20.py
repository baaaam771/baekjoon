n = int(input())

unit1 = '*'+ ' '
unit2 = ' '+ '*'
line1 = unit1*n
line2 = unit2*n

for i in range(n//2):
    print(line1)
    print(line2)
if n % 2 == 1:
    print(line1)