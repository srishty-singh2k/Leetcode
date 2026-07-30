class Solution(object):
    def groupAnagrams(self, strs):
        sortedMap = defaultdict(list)
        for str in strs:
            sortedS = ''.join(sorted(str))
            sortedMap[sortedS].append(str)
        return sortedMap.values()