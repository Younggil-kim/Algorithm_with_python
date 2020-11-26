stringA = input().lower()
stringB = input().lower()

lstA = [0]*26
lstB = [0]*26


for i in stringA:
    lstA[ord(i) - 97] += 1

for i in stringB:
    lstB[ord(i)-97] += 1

print(lstA)
print(lstB)


if len(lstA) == len(lstB): #길이가 같은경우
    for i in range(26):
        if lstA[i] - lstB[i] < 0:  # 마이너스일경우
            lstA[i] = abs(lstA[i] - lstB[i])
        elif lstA[i] == lstB[i]:
            lstA[i] = lstA[i] - lstB[i]
        else:  # 리스트 A가 더 클경우
            lstA[i] = lstA[i] - lstB[i]
    print(sum(lstA)//2)
elif len(lstA) > len(lstB): #A의 길이가 더 큰 경우 #교체와 삭제
    for i in range(26):
        lstA[i] = abs(lstA[i] - lstB[i])
