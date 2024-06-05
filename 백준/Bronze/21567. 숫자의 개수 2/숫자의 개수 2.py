a = int(input())
b = int(input())
c = int(input())

dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
fin = list(str(a*b*c))

for i in fin:
    dict[i] += 1

# print(dict)
for i in range(10):
    print(dict[str(i)])