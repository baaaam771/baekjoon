n = int(input())
a = set(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in a:
        print("1")
    else:
        print("0")