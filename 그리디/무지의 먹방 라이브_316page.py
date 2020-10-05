#효울성 전부 탈락
# 정확성에서는 두 문제만 시간초과
#여기서 좀 더 효율적으로 짜보자

def solution(food_times, k):
    answer = 0
    cnt = 0
    #2초에 오류가 나는거면 2번 먹은거고
    #3초에 오류가 나는거면 3번은 먹은거야
    #그러니까 끝까지 돌 필요 없고
    #K번만 돌면 됨인데, 0이 추가되면 0만큼 더돌아야해
    #K번 돌면서 0이 되면 -1하는거고
    #남아있으면 다음음식 출력하는거야
    len_food_times = len(food_times)
    while True:
        for i in range(len_food_times):
            if food_times[i] != 0:#음식이 있으니까
                food_times[i] -= 1#음식 섭취
                cnt = cnt + 1#카운트 세어 주고
                if cnt == k:# 만약에 오류가 났으면
                    j = i + 1#다음접시
                    if j == len_food_times: #근데 길이를 넘어버리면
                        j = 0 #0부터 다시
                    while True:
                        if food_times[j] == 0:#다음 접시가 비어있으면
                            j = j + 1# 다음 접시를 가져와
                            if j == len_food_times: #근데 길이를 넘어버리면
                                j = 0 #0부터 다시
                        else:
                            answer = j + 1
                            return answer
                elif food_times.count(0) == len_food_times:
                    answer = -1
                    return answer

#다시생각해보자
#하나하나 반복을 해버리니까 시간초과를 받아
# 그럼 일단, 정렬을 시켜놓고, 생각해볼까
#