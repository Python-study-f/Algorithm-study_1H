#from collections import Counter

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         ans = []
#         lst = Counter(nums)
#
#         lst_ = lst.most_common(k)
#
#         for i in range(k):
#             ans.append(lst_[i][0])
#
#         return ans
'''
1. collections 모듈에서 Counter 사용
2. moost_common 메서드를 통해서 k개수만큼 리스트에 넣음
3. 리스트 반환
'''



# import operator
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#
#         dic = {}
#         lst = []
#         ans = []
#
#         for num in nums:
#             if dic.get(num) is None:
#                 dic[num] = 1
#             else:
#                 dic[num] += 1
#         for key, value in dic.items():
#             lst.append([key, value])
#
#         lst = sorted(lst, key=lambda x: -x[1])
#
#         for i in range(k):
#             ans.append(lst[i][0])
#
#         return ans
'''
1. Count 사용안하고 dictionary에 넣음
2. dictionary 넣고 key,value를 list에 넣음
3. sort 람다식으로 때리고 반환
'''