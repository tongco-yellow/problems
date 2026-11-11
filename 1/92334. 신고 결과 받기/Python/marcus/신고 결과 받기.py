def solution(id_list, report, k):
    reported = {}
    reporting = {}
    answer_dict = {}
    answer = []
    for a in id_list:
        reported[a] = 0
        reporting[a] = []
        answer_dict[a] = 0
        
    for i in range(len(report)):
        rpt, rptd = report[i].split()
        if not rpt in reporting[rptd]:
            reported[rptd] += 1
            reporting[rptd].append(rpt)
    
    for b in id_list:
        if reported[b] >= k:
            for c in reporting[b]:
                answer_dict[c] += 1
    
    for d in id_list:
        answer.append(answer_dict[d])
            
    
    
    
    return answer