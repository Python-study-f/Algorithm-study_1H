class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}

        for st in strs:

            key = ''.join(sorted(st))
            if key not in dic:
                dic[key] = []
            dic[key].append(st)

        ret = []
        for key in dic:
            ret.append(dic[key])

        return ret