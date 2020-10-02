#문제 해석 #시작 시간 AM 1:14
# 0과 1로만 이루어진 문자열 S가 있을 때, 문자열 S에 있는 모든 숫자를 전부 같ㅌ게 만드려고 한다.
# 행동은 S에서 연속된 하나 이상의 숫자를 잡고, 모두 뒤집는것
# 예로 S = 0001100 이면, 전체로 뒤집어서 1110011로 바꾸고, 4,5번째를 바꾸는것
#하지만 처음부터 4~5를잡아서 뒤집으면 한번에 다 바꿔짐
# 최소를 출력해라
#어떻게 해야 할까?
# 0100010
# 1011101
#0이되는 경우와, 1이되는 경우를 나누어서 횟수를 비교하고 적은거 출력


import sys

string_0 = sys.stdin.readline()
string_1 = string_0

all_zero = 0
all_one = 0

string_0 = string_0.split("0")
string_1 = string_1.split("1")

for i in string_0:
    if "1" in i:
        all_zero = all_zero+1

for i in string_1:
    if "0" in i:
        all_one = all_one + 1

print(min(all_one,all_zero))