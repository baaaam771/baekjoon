arr = list(input())
if arr[-1] == '0' and arr[-2] == '1' and len(arr) >= 3:
    a_arr = arr[:-2]
    b_arr = arr[-2:]
    # print(a_arr)
    # print(b_arr)
    a = int("".join(a_arr))
    b = int("".join(b_arr))


else:
    a_arr = arr[:-1]
    # print(a_arr)
    a = int("".join(a_arr))
    b = int(arr[-1])

print(a + b)