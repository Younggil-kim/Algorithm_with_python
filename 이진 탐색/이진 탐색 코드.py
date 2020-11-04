def binary_search(array, target, start, end):
    if start > end:
        return None
    else:
        mid = (start+end) //2
        if array[mid] == target:#값이 맞는경우
            return mid
        elif array[mid] > target:#찾고자 하는 타겟이 작은경우
            return binary_search(array,target,start,mid-1)
        else:#찾고자 하는 타겟이 큰 경우
            return binary_search(array,target,mid+1, end)


#반복문
def binary_search1(array, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None