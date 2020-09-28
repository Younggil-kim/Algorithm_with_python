#시작 시간 AM 1:00
#종료 시간 AM 1:10
#문제 해석
# 각 자리가 숫자 0에서 9로만 이루어진 문자열 S가 있을 떄, 왼쪽부터 시작해서,
# * 혹은 +연산자를 넣어 결과적으로 만들수 있는 수 중 가장 큰 수를 구하는 프로그램을 작성해라
# 예를들어 02984면 0 + 2 * 9 * 8이 가장 크다.

#0과 1이 나오면 그 다음거는 더해주고,
# 아니면 다 곱해주면 될 거같다.

string = input()
lst = list()

for i in string:
    if i == '0' or i == '1':
        lst.append(i)
        lst.append('+')
    else:
        lst.append(i)
        lst.append('*')

print(lst)
result = ''.join(lst[0:-1])
print(eval(result))
