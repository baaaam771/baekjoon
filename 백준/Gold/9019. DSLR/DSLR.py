import sys
from collections import deque


def solve(A, B):
    visited1 = [ "" ] * 10000
    visited2 = [ "" ] * 10000
    queue = deque()
    queue.append((A, 1))
    queue.append((B, 2))
    
    while queue:
        cur, type = queue.popleft()
        
        if type == 1:
            operations = [
                ((2 * cur) % 10_000, 'D'),
                ((cur - 1) % 10000, 'S'),
                (((cur % 1000) * 10 + (cur//1000)), 'L'),
                (((cur % 10) * 1000 + (cur // 10)), 'R'),
            ]
            
            for next, operation in operations:
                if visited1[next] != "" or next == cur: continue
                queue.append((next, type))
                visited1[next] = ''.join((visited1[cur], operation))
                
                if next == B: return visited1[next]
                elif visited1[next] != "" and visited2[next] != "":
                    return ''.join((visited1[next], visited2[next]))

        else: # 역방향 탐색
            operations = [
                (cur // 2, 'D'),
                ((cur + 10000) // 2, 'D'),
                (0 if cur == 9999 else cur + 1, 'S'),
                (((cur % 10) * 1000 + (cur // 10)), 'L'),
                (((cur % 1000) * 10 + (cur//1000)), 'R'),
            ]
            
            for next, operation in operations:
                if visited2[next] != "" or next == cur: continue
                if operation == "D" and cur % 2 != 0: continue
                queue.append((next, type))
                visited2[next] = ''.join((operation, visited2[cur]))
                
                if next == A: return visited2[next]
                elif visited1[next] != "" and visited2[next] != "":
                    return ''.join((visited1[next], visited2[next]))
            

for T in range(int(input())):
    A, B = map(int,sys.stdin.readline().rstrip().split())
    print(solve(A, B))
