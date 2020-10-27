def solution(N, stages):
    answer = []
    len_stages = len(stages)
    for i in range(1,N+1):
        if i == N:
            i = i + 1
            con = stages.count(i-1)#진행중
            answer.append([i-1, con/len_stages])
        else:
            con = stages.count(i)#진행중
            answer.append([i, con/len_stages])
        len_stages -= con
        if len_stages == 0:#0으로 나눠지는경우
            for j in range(i+1,N+1):
                answer.append([j, 0])
            break
    answer.sort(key=lambda x:(-x[1],x[0]))
    result = []
    for i in answer:
        result.append(i[0])
    return result