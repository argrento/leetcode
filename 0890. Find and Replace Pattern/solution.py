class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            mask1, mask2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in mask1: 
                    mask1[w] = p
                if p not in mask2: 
                    mask2[p] = w
                if (mask1[w], mask2[p]) != (p, w):
                    return False
            return True
        return filter(match, words)
