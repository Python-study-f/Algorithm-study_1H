def solution(answers):
    answer = []
    count = [0, 0, 0]  # 맞춘 개수
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if a[i % len(a)] == answers[i]:  # answers 길이 % a,b,c 길이
            count[0] += 1
        if b[i % len(b)] == answers[i]:
            count[1] += 1
        if c[i % len(c)] == answers[i]:
            count[2] += 1
    tuple_count = [(1, count[0]), (2, count[1]), (3, count[2])]
    tuple_count.sort(key=lambda x: x[1], reverse=True)  # 내림차순 - 높은 점수가 젤 첫번째 값으로 올 수 있게 함
    answer.append(tuple_count[0][0])
    for i in range(1, len(tuple_count)):  # 동점자가 있을 때
        if tuple_count[i][1] != tuple_count[i - 1][1]:  # 동점이 아닐 때
            break
        answer.append(tuple_count[i][0])  # 동점일 경우 추가된다
    answer.sort()  # 여럿일 경우, 오름차순 정렬
    return answer
