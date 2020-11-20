
#2,3,5에다가 235를 계속 곱해야함
# 4  6  10  6  9 15
lst = [1,2,3,5]
N = int(input())
plg = 0
while True:
    for i in lst:
        if 2*i not in lst:
            lst.append(2*i)
        if 3*i not in lst:
            lst.append(3*i)
        if 5 * i not in lst:
            lst.append(5*i)
        if 1000 in lst:
            plg = 1
            break
    if plg == 1:
        break
lst.sort()
print(lst[N-1])