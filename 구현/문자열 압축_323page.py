#받아온 문자열을 1,2,3,4씩 먼저 쪼갠 다음에
# 중복 검사를 해서 최소값을 뽑는다.
# 이거 한문제 런타임에러뜨는거 빼고 전부 맞는데
#런타임 에러가 뭔지 모르겠어

# 글자가 한글자일때 런타임 에러였어
#그래서 한글자일때 예외처리하는 코드 추가함
def solution(s):
    global answer
    len_s = len(s)
    lst = list()
    if len_s == 1:#한글자인경우
        answer = 1
        return answer
    for j in range(1,len_s//2 + 1):
        num = 1
        result = ""
        length = j
        splt = [s[i:i+length] for i in range(0, len_s, length)]
        for i in range(1,len(splt)):
            if splt[i-1] == splt[i]:
                num = num + 1
            else:
                if num != 1:
                    result = result + str(num) + splt[i-1]
                    num = 1
                else:
                    result = result + splt[i-1]
        if num != 1:
            result = result + str(num) + splt[i]
        else:
            result = result + splt[i]
        lst.append(len(result))
        print(result)
    answer = min(lst)
    return answer

a =solution("a")
print(a)