def m_time(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m

def solution(schedule):
    answer = 0

    used = []

    def make_schedule(idx):
        nonlocal answer
        if idx == 5:
            answer += 1
            return
        for sch in schedule[idx]:
            sp_sch = sch.split()
            if len(sp_sch) == 2:
                temp_start = m_time(sp_sch[1])
                for w, start_t, end_t in used:
                    if w != sp_sch[0]:
                        continue
                    if temp_start < start_t and temp_start + 180 <= start_t:
                        continue
                    if temp_start >= end_t and temp_start + 180 > end_t:
                        continue
                    break
                else:
                    used.append([sp_sch[0], temp_start, temp_start + 180])
                    make_schedule(idx + 1)
                    used.pop()

            else:
                w1, t_start, w2, t_start2 = sp_sch[0], m_time(sp_sch[1]), sp_sch[2], m_time(sp_sch[3])
                for w, start_t, end_t in used:
                    if w1 != w:
                        if w2 != w:
                            continue
                        else:
                            if t_start2 < start_t and t_start2 + 90 <= start_t:
                                continue
                            if t_start2 >= end_t and t_start2 + 90 > end_t:
                                continue
                            break
                    else:
                        if w2 != w:
                            if t_start < start_t and t_start + 90 <= start_t:
                                continue
                            if t_start >= end_t and t_start + 90 > end_t:
                                continue
                        else:
                            if t_start < start_t and t_start + 90 <= start_t:
                                if t_start2 < start_t and t_start2 + 90 <= start_t:
                                    continue
                                if t_start2 >= end_t and t_start2 + 90 > end_t:
                                    continue
                                break
                            if t_start >= end_t and t_start + 90 > end_t:
                                if t_start2 < start_t and t_start2 + 90 <= start_t:
                                    continue
                                if t_start2 >= end_t and t_start2 + 90 > end_t:
                                    continue
                                break
                else:
                    used.append([w1, t_start, t_start + 90])
                    used.append([w2, t_start2, t_start2 + 90])
                    make_schedule(idx + 1)
                    used.pop()
                    used.pop()

    make_schedule(0)


    return answer