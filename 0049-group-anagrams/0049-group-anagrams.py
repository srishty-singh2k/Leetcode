class Solution(object):
    def groupAnagrams(self, strs):
        # m=no of strings, n=longest string
        #TC=O(m*n) SC=O(m*n)
        res = defaultdict(list)
        for s in strs:
            counter = [0]*26
            for c in s:
                counter[ord(c)-ord('a')] += 1
            res[tuple(counter)].append(s)
        return list(res.values())

        #TC=O(m*n logn) SC=O(m*n)
        # sortedMap = defaultdict(list)
        # for str in strs:
        #     sortedS = ''.join(sorted(str))
        #     sortedMap[sortedS].append(str)
        # return sortedMap.values()
        
