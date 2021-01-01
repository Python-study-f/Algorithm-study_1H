def solution(n):
    answer = []
    l = len(n)
    for i in range(l):
        for j in range(l):
            if n[i] != n[j]:
                answer.append(n[i] + n[j])
            elif n[i] == n[j] and i != j:
                answer.append(n[i] + n[j])
    return sorted(list(set(answer)))