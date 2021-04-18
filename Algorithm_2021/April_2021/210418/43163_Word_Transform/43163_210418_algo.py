def solution(begin, target, words):
    answer = 0 
    stacks = [begin]
    visited = {i:0 for i in words}
  #  print(visited)
    if target not in words:
        return 0
    while stacks:
        stack = stacks.pop()
        if stack == target:
            return answer
        
        for word in words:
            for i in range(len(word)):
                copy = list(word)
                copy_front = list(stack)
                
                copy[i] = 0
                copy_front[i] = 0
                if copy == copy_front:
                    if visited[word] != 0: #visited가 1이라면 이미 검사했던 단어므로 그냥 넘어간다.
                        continue
                    visited[word] = 1  #visited가 0이면 해당 단어의 visited 값을 1로 바꾼다.
                    stacks.append(word)
                    break
        answer += 1 #Depth 1추가

    return answer
