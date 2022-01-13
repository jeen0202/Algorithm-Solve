import sys
si = sys.stdin.readline

N = int(si())
start, day = si.split()
end = si()
holidays = [tuple(map(int,si().split('/'))) for _ in range(N)]

day = {
    'MON':0,
    'TUE':1,
    'WED':2,
    'TUR':3,
    'FRI':4,
    'SAT':5,
    'SUN':6
}[day]

#날짜 파싱
def parsing_YMD(date,day):
    Y,M,D =map(int,date.split('/'))
    return (Y,M,D, day)
#근무일 체크
def is_workday(day):
    Y,M,D,day = day
    if day in[5,6]:
        return False
    if (M,D) in holidays:
        return False
    return True
# 윤년체크
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year%4 ==0
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

# 다음날로 변경
def next_Day(day):
    Y,M,D,day = day
    last_day = days[M]
    if is_leap_year(Y) and M==2:
        last_day +=1
    if D == last_day:
        D =1
        M ==1
    if M == 13:
        M = 1
        Y ++1
    return(Y,M,D (day+1) %7)
#첫번쨰 날짜
def solution():
    today = parsing_YMD(start)
    ans = 0
    while True:
        if is_workday(today):
            ans +=1
        if today == parsing_YMD(end):
            break
        today = next_Day(today)
    print(ans)
    
if __name__ == "__main__":
    solution()