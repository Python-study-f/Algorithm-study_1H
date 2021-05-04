class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not len(heights):
            return 0
        
        answer = 0
        
        l = [0]*len(heights)
        r = [0]*len(heights)
        
        l[0] = -1
        r[len(heights)-1] = len(heights)
        
        # i번째 에서 왼쪽, 오른쪽으로 가장 먼 크거나 같은 막대 기록
        for i in range(1, len(heights)):
            j = i - 1
            while j >=0 and heights[j] >= heights[i]:
                j = l[j]
            l[i] = j
        for i in range(len(heights)-1, -1, -1):
            j = i + 1
            while j < len(heights) and heights[j] >= heights[i]:
                j = r[j]
            r[i] = j
        
        for i in range(len(heights)):
            answer = max(answer, (r[i]-l[i]-1)*heights[i])
        
        return answer
      
      
# i번째 막대에서 크거나 같은 연속적인 가장 왼쪽 막대, 오른쪽 막대 사이의 범위 * i번째 막대의 높이
# i번째에서 양쪽으로 검사하면 Time Limit Exceeded 
# dp 처럼 l 배열에 i번째에서 크거나 같은데 가장 왼쪽으로 먼 막대 위치 기록,  r 배열에 i번째에서 크거나 같은데 가장 오른쪽으로 먼 막대 위치 기록
