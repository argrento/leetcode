class Solution:
    def reverse_helper(self, s: List[str], left: int, right: int):
        while left < right:
            s[left], s[right] = s[right], s[left]
            right -= 1
            left += 1
        
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse full list
        self.reverse_helper(s, 0, len(s)-1)
        
        word_start, word_end = 0, 1
        while word_end <= len(s):
            if word_end == len(s) or s[word_end] == ' ':
                self.reverse_helper(s, word_start, word_end-1)
                word_start = word_end + 1
            word_end += 1
