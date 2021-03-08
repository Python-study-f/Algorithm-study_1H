class Solution:
    # 524 ms	18.4 MB
    # https://leetcode.com/problems/daily-temperatures/submissions/
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # init
        stack = []
        result = [0] * len(T)

        for idx, value in enumerate(T):
          #print(T[idx] , T[idx-1])

            # stack이 있을경우만 검사
            while stack:
              # 스택에 새로 들어갈 값이 top보다 큰경우
              if T[idx] > T[stack[-1]]:
                #print(stack[-1], idx)
                place = stack.pop()
                result[place] = (idx - place)
              # 아닐경우 push 해야하니 break
              else:
                break
            stack.append(idx)
        return result