#효율성 테스트에서 2개 틀려서 75점 받은 코드
#나는 해당되는 범위를 찾아놓고 다시 거기서 단어 길이 맞는걸 찾아줬는데
#애초에 처음부터 길이를 나눠놓으면 더 효율적으로 작동할 듯 하다.
from bisect import bisect_left, bisect_right

def rangeWords(words, start, end):
    a = bisect_left(words, start)
    b = bisect_right(words, end)
    return (a, b)


def solution(words, queries):
    answer = []
    reverseList = list()
    len_words = len(words)
    for i in range(len_words):
        reverseList.append(words[i][::-1])
    reverseList.sort()
    words.sort()
    cnt = 0
    for i in range(len(queries)):
        if queries[i][0] != "?":
            (start, end) = rangeWords(words, queries[i].replace("?", "a"), queries[i].replace("?", "z"))
            for j in words[start:end]:
                if len(queries[i]) == len(j):
                    cnt = cnt + 1
            answer.append(cnt)
            cnt = 0
        else:
            (start, end) = rangeWords(reverseList, queries[i][::-1].replace("?", "a"),
                                      queries[i][::-1].replace("?", "z"))
            for j in reverseList[start:end]:
                if len(queries[i]) == len(j):
                    cnt = cnt + 1
            answer.append(cnt)
            cnt = 0
    return answer

#다시 짜자
from bisect import bisect_left, bisect_right

def rangeWords(words, start, end):
    a = bisect_left(words, start)
    b = bisect_right(words, end)
    return b-a


def solution(words, queries):
    answer = []
    word = [[]for _ in range(10001)]
    reverseList = [[]for _ in range(10001)]

    for i in words:
        word[len(i)].append(i)
        reverseList[len(i)].append(i[::-1])

    for i in range(10001):
        reverseList[i].sort()
        words[i].sort()

    for i in range(len(queries)):
        if queries[i][0] != "?":
            cnt = rangeWords(words[len(queries[i])], queries[i].replace("?", "a"), queries[i].replace("?", "z"))
            answer.append(cnt)
        else:
            cnt = rangeWords(reverseList[len(queries[i])], queries[i][::-1].replace("?", "a"), queries[i][::-1].replace("?", "z"))
            answer.append(cnt)
    return answer