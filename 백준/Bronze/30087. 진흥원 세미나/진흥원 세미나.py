# 세미나 주제와 교실 번호를 저장하는 딕셔너리
seminar_rooms = {
    "Algorithm": 204,
    "DataAnalysis": 207,
    "ArtificialIntelligence": 302,
    "CyberSecurity": "B101",
    "Network": 303,
    "Startup": 501,
    "TestStrategy": 105
}

# 첫 번째 줄에 진흥이가 신청한 세미나의 수 N을 입력받음
N = int(input().strip())

# N개의 줄에 걸쳐 세미나 주제를 입력받고 해당 교실 번호를 출력
for _ in range(N):
    seminar = input().strip()
    print(seminar_rooms[seminar])