#문제 해석
#두 배열이 있는데, 최대 K번 바꿔치기를 해서 배열 A의 합이 가장 크게 나오도록 하라

#간단한듯? A정렬, B는 역정렬 후 K인덱스까지 교체하면 끝

N, K = map(int, input().split())

lstA = list(map(int,input().split()))
lstB = list(map(int,input().split()))

lstA.sort()
lstB.sort(reverse=True)

for i in range(K):
    lstA[i] = lstB[i]

print(sum(lstA))