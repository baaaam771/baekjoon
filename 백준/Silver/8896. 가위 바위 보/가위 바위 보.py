def solve():
    n = int(input())
    s = []
    alive = [True] * (n + 1)

    for i in range(1, n + 1):
        s.append(input().strip())

    k = len(s[0])
    
    for i in range(k):
        rsp = [0] * 3
        
        for j in range(n):
            if not alive[j]:
                continue
            if s[j][i] == 'R':
                rsp[0] = 1
            elif s[j][i] == 'S':
                rsp[1] = 1
            elif s[j][i] == 'P':
                rsp[2] = 1
        
        if sum(rsp) == 2:
            if rsp[0] == 0:
                lose_char = 'P'  # S vs P
            elif rsp[1] == 0:
                lose_char = 'R'  # P vs R
            elif rsp[2] == 0:
                lose_char = 'S'  # R vs S
            
            for j in range(n):
                if s[j][i] == lose_char:
                    alive[j] = False
    
    cnt = 0
    ans = 0
    
    for i in range(n):
        if alive[i]:
            cnt += 1
            ans = i + 1  # 1-based index
    
    if cnt != 1:
        ans = 0
    
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
