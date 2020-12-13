def compress(string):
    result = ""
    cnt = 1
    #1번과 2번이 같으면 cnt + 2
    #이후 2번과 3번으로 넘어감
    #1번과 2번이 다르면 result + 1번
    #이후2번과 3번으로 넘어감
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            cnt = cnt + 1
        else:
            if cnt == 1:#다른데, 누적값이 없는 경우
                result = result + string[i]
            else:#다른데 누적값이 있는 경우
                result = result + str(cnt) + string[i]
                cnt = 1#카운트 초기화 
    if cnt == 1:#마지막 값은 따로 처리 해 줌, 마지막 값이 다른경우
        result = result + string[-1]
    else:#마지막 값이 같은 경우
        result = result + str(cnt) + string[-1]
    return result

def solution(s):
    #먼저 문자열 길이가 1인 경우 그대로 반환
    if len(s) == 1:
        return 1
    #문자열을 받아서, 1자리 ~ 길이의 반까지 자른 후, result에 저장
    #이후 min으로 최소값 받아와서 반환할 것
    result = list()
    for i in range(1,len(s)//2+1):
        slicing = [s[j:j+i] for j in range(0, len(s), i)]
        string = compress(slicing)
        result.append(len(string))
    answer = min(result)
    return answer