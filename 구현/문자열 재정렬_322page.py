#시간제한 20분 시작시간 AM 00: 23

#문제 해석
#스트링이 들어오면, 문자는 문자대로 정렬, 숫자는 더해서 문자열 마지막에 넣어서 출력해주기

s = input()
num_list = [0,1,2,3,4,5,6,7,8,9]
al_list = list()
sum_number = 0
for i in s:
    if i.isalpha():#알파벳인지 아닌지 판단해주는 거
        al_list.append(i)
    else:
        sum_number += int(i)
al_list.sort()
result = "".join(al_list)+ str(sum_number)
print(result)