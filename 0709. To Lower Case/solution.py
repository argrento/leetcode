class Solution:
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        for idx, letter in enumerate(s):
            if letter >= 'A' and letter < 'a':
                s[idx] = chr(ord(letter) + 32)
                
        return "".join(s)
