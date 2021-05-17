class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_position = {}
        result = 1
        
        for w in sorted(words, key=len):
            word_position[w] = 1
            for idx in range(len(w)):
                previous = w[:idx] + w[idx + 1:]
                
                if previous in word_position:
                    word_position[w] = max(word_position[w], word_position[previous] + 1)
                    result = max(result, word_position[w])
                    
        return result
        
