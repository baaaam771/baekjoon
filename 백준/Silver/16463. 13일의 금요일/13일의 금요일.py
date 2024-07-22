def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    
    count = 0
    day = 1  # 2019년 1월 1일은 화요일 (0: 월요일, 1: 화요일, ..., 6: 일요일)
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for year in range(2019, n + 1):
        for month in range(1, 13):
            if (day + 12) % 7 == 4:  # 13일이 금요일인지 확인
                count += 1
            if month == 2:  # 2월 처리
                if is_leap_year(year):
                    day += 29
                else:
                    day += 28
            else:
                day += month_days[month]
    
    print(count)

if __name__ == "__main__":
    main()
