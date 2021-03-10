from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        str_dic = defaultdict(list)

        for i in range(len(strs)):
            key = sorted(list(strs[i]))
            strs[i] = [tuple(key), strs[i]]

            str_dic[tuple(key)].append(strs[i][1])

        results = list(str_dic.values())[::-1]

        for i in range(len(results)):
            results[i].sort()

        return results