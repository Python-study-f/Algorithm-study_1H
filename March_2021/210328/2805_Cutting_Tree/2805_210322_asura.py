# import sys
#
# input = sys.stdin.readline
#
# def find_target(arr,height):
#     total = 0
#
#     for i in range(len(arr)):
#         if arr[i] - height <= 0:
#             continue
#         else:
#             total += arr[i] - height
#     return total
#
#
# def binary_search(arr,target,start,end):
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if target == find_target(arr,mid):
#             return mid
#
#         elif target < find_target(arr,mid):
#             end = mid -1
#
#         else:
#             start = mid+1
#     return None
#
# N, M = map(int, input().strip().split())
#
# data = list(map(int, input().split()))
# data.sort()
#
# print(binary_search(data,M,data[0],data[-1]))
'''
똥고생 ㅅㄱ
'''

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
datas = list(map(int,input().split()))
datas.sort()

left = 0
right = max(datas)
height = 0

while left <= right:
    getHeight = 0
    mid = (left + right) // 2

    for data in datas:
        if data - mid < 0:
            continue
        getHeight += data-mid

    if getHeight == M:
        print(mid)
        sys.exit()
    elif getHeight < M:
        right = mid-1
    else:
        if height < mid:
            height = mid
        left = mid +1

print(height)


