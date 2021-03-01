# class Solution:
#    def dailyTemperatures(self, T: List[int]) -> List[int]:
#         ret = []
#
#         for i in range(len(T)):
#             cnt = 0
#             for j in range(i,len(T)):
#                 if T[i] < T[j]:
#                     ret.append(j-i)
#                     break
#             else:
#                 ret.append(0)
#          return ret
#       Solution = Brute Force O(N^2)  , range [1, 30000] 3만 * 3만 = 9억  범위 초과


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        st = []
        ans = [0 for _ in range(len(T))]


        for idx, cur in enumerate(T):
            while st and cur > T[st[-1]]:
                last = st.pop()
                ans[last] = idx - last
            st.append(idx) # T의 인덱스 값이 들어간다.
        return ans


#       Solution = Transformed Brute Force O(N) < O(ㅁ) < O(N^2)




''' 문제 해결 방식

1. for(for()) 루프로 O(N^2) 해결 but, range 30000이므로 범위초과 nxn > 1억이므로
2. for문 하나로 O(N) 시간복잡도를 풀어보려고 했으나, 한참 고민 후, 불가능하다는 것을 판단
3. 그래서 O(N^2)에서 변형을 하면 시간초 내에 들어 갈 것이라고 생각.

'''