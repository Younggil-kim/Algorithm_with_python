#들어오는 숫자 반반 나눠서 왼쪽자리수 합, 오른쪽 자리수 합이 같으면 럭키 아니면 레디


N = input()
gage = 0

for i in range(len(N)):
    if i < len(N)//2:
        gage = gage + int(N[i])
    else:
        gage = gage - int(N[i])

if gage == 0:
    print("LUCKY")
else:
    print("READY")