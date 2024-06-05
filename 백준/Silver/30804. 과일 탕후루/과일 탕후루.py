# n = int(input())
# fru = list(map(int, input().split()))
# # print(fru)

# count = 0
# end = 0

# def check(arr):
#     temp = set(arr)
#     return len(temp)

# for start in range(n):
#     while check(fru[start:end+1]) < 3 and end < n:
#         end += 1
#     if len(fru[start:end]) > count:
#         count = len(fru[start:end])

# print(count)
    
n = int(input())
fru = list(map(int, input().split()))

count = 0
end = 0
unique_count = {}
max_length = 0

for start in range(n):
    while end < n and len(unique_count) < 3:
        if fru[end] in unique_count:
            unique_count[fru[end]] += 1
        else:
            unique_count[fru[end]] = 1
        end += 1
    
    if len(unique_count) >= 3:
        max_length = max(max_length, end - start - 1)
    else:
        max_length = max(max_length, end - start)
    
    unique_count[fru[start]] -= 1
    if unique_count[fru[start]] == 0:
        del unique_count[fru[start]]

print(max_length)
