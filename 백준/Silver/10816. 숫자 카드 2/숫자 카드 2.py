n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_dict = {}
for i in n_list:
    if i in n_dict:
        n_dict[i] += 1
    else:
        n_dict[i] = 1

ans = []
for i in m_list:
    if i in n_dict:
        ans.append(n_dict[i])
    else:
        ans.append(0)

print(' '.join(map(str, ans)))
