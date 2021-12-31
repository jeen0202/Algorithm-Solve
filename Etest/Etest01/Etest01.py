import datetime as dt
def solution(schedule):
    answer=  0
    date = ["MO","TU","WE","TH","FR"]
    for i in range(len(schedule[0])):
        sday,stime = [],[]
        if len(schedule[0][i])<=8:            
            sday.append(date.index(schedule[0][i].split()[0]))  
            stime.append(dt.datetime.strptime(schedule[0][i].split()[1],"%H:%M"))          
            #print(sday,stime) 
        else :
            sday = [date.index(schedule[0][i].split()[0]), date.index(schedule[0][i].split()[2])]
            stime = [dt.datetime.strptime( schedule[0][i].split()[1],"%H:%M"),dt.datetime.strptime(schedule[0][i].split()[3],"%H:%M")]
            #print(sday,stime)     
        for s in schedule[1:]:
            for no in s :                
                if len(no)<=8:
                    time=dt.datetime.strptime(no.split()[1],"%H:%M")
                    if date.index(no.split()[0]) not in sday and abs(stime[0]-time)>=dt.timedelta(hours=3):
                        answer+=1                    
                else:
                    day = [date.index(no.split()[0]),date.index(no.split()[2])]
                    time = [dt.datetime.strptime(no.split()[1],"%H:%M"),dt.datetime.strptime(no.split()[3],"%H:%M")]
                    count = 0
                    for j in range(1):
                        if day[j] == sday[j] and abs(stime[j]-time[j])>=dt.timedelta(hours=3):
                            count +=1
                    if count == 2:
                        answer +=1
    return answer

if __name__ == '__main__':    
    print(solution([["MO 12:00 WE 14:30", "MO 12:00", "MO 15:00", "MO 18:00"], ["TU 09:00", "TU 10:00", "TU 15:00", "TU 18:00"], ["WE 09:00", "WE 12:00", "WE 15:00", "WE 18:00"], ["TH 09:30", "TH 11:30", "TH 15:00", "TH 18:00"], ["FR 15:00", "FR 15:00", "FR 15:00", "FR 15:00"]]))

