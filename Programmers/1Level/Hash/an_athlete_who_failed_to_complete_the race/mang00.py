def solution(participant, completion):
    d_p = to_dic(participant)
    d_c = to_dic(completion)
    for name in d_p.keys():
        if name in d_c:
            d_p[name] -= d_c[name]
        else:
            return name  # 완주한 사람 목록에 해당 사람이 없을 때
    return list(dict(filter(lambda x: x[1] > 0, d_p.items())).keys())[0]


def to_dic(source):
    d = {}
    for name in source:
        d[name] = source.count(name)
        # if name in d:
        #     d[name] += 1
        # else:
        #     d[name] = 1
    return d