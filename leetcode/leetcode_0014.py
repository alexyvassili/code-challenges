def get_prefix(word1, word2):
    ix = 0
    for i, j in zip(word1, word2):
        if i == j:
            ix += 1
        else:
            break
    return word1[:ix] if ix else ""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        pref = get_prefix(strs[0], strs[1])
        for s in strs[2:]:
            if not pref:
                break
            pref = get_prefix(pref, s)
        return pref
