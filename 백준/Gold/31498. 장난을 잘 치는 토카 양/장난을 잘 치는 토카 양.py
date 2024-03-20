import sys, math
input = sys.stdin.readline
a, b = map(int, input().split())
c, d = map(int, input().split())
k = int(input())

def doldol_walk(n):
    doldol = (a + c) - d*n
    if doldol < 0:
        return 0
    else:
        return doldol

def toka_home_check():
    # 줄어드는 속도에 의해 이동하는 거리가 0이 될때
    chk = b//k +1
    last_toka = a -b*chk + 0.5*k*(chk)*(chk-1)
    # 줄어드는 속도에 의해 이동하는 거리가 0이 될때 
    # 아직 집에 도착하지 못함 
    if last_toka > 0:
        return False
    else:
        return True

def toka_walk_home(n):
    to_home = a -b*n + 0.5*k*(n)*(n-1)
    if to_home < 0:
        return 0
    else:
        return to_home

def toka_walk_home_no_k(n):
    to_home = a -b*n
    if to_home < 0:
        return 0
    else:
        return to_home

# 토카가 집에 도착할때
def find_last_toka():
    left, right = 1, b // k +1
    while left <= right:
        mid = (left + right)//2  
        # print(left, right, mid) 
        if toka_walk_home(mid)>0:
            left = mid + 1        
            # right = mid - 1
        else:
            get = mid
            right = mid - 1
            # left = mid + 1
    # print(left)        
    return get


def find_last_toka_no_k():    
    if a%b == 0:
        return a//b
    else:
        return a//b+1

# k가 0일때 div0가 나오기 때문에 따로 설정
if k == 0:

    last = find_last_toka_no_k()
    if doldol_walk(last) - toka_walk_home_no_k(last)>0:
        print(last)
    else:
        print(-1)

else:
    if toka_home_check() == True:
        left, right = 1, find_last_toka()
        if doldol_walk(right)-toka_walk_home(right)>0:       
            print(right)
        # 돌돌이가 토카를 잡음
        else:
            print(-1)

    #토카가 중간에 멈춤 -> 돌돌이가 집갈때 까지를 end로(a+c//d)
    else:
        print(-1)





