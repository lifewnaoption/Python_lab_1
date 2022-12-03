class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            ss = "".join(sorted(s))
            res[ss].append(s)
        return [ v for i, v in res.items()]