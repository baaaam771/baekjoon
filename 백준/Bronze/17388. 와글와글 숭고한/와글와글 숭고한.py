S, K, H = map(int, input().split())
tot = []
tot.append(S)
tot.append(K)
tot.append(H)

if sum(tot) >= 100:
    print("OK")
else:
    if min(tot) == S:
        print("Soongsil")
    elif min(tot) == K:
        print("Korea")
    else:
        print("Hanyang")