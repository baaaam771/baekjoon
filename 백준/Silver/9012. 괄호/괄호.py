n = int(input())
ans=[]
for i in range(n):
    sym = list(input())

    array = []

    for i in sym:
        if i == '(':
            array.append("(")
        else:
            if "(" in array:
                array.pop()
            else:
                array.append(")")

    if len(array) == 0:
        ans.append("YES")
    else:
        ans.append("NO")

for i in ans:
    print(i)