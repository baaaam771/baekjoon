dict = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0}
total = 0
mul = 0 
for i in range(20):
    _, h, g = input().split()
    if g in dict:
        mul += float(h) * dict[g]
        total += float(h)

print(mul/total)
