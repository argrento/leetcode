from itertools import cycle

class Solution:
    def line_length(self, line: List[str]) -> int:
        return sum([len(s) for s in line])
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = [words[0]]
        
        # pack words to lines
        for word in words[1:]:
            # check if we can add a word to a line
            free_space = maxWidth - self.line_length(current_line)
            if len(word) < free_space:
                # add a space between words if there is a word before the new one
                current_line.extend([' ', word])
            else:
                if len(current_line) == 1 and maxWidth - self.line_length(current_line) != 0:
                    current_line.append(' ')
                result.append(current_line)
                current_line = [word]
        
        # align last line
        last_line = "".join(current_line)
        while len(last_line) != maxWidth:
            last_line += ' '
                
        for line_idx, line in enumerate(result):
            whitespaces = maxWidth - self.line_length(line)
            if whitespaces == 0:
                continue
            word_it = cycle(line)
            word = next(word_it)
            word_idx = 0
            while whitespaces > 0:
                if ' ' in word:
                    result[line_idx][word_idx] += ' '
                    whitespaces -= 1
                word = next(word_it)
                word_idx = (word_idx + 1) % len(line)
                
        
        result.append([last_line])
                
        return ["".join(line) for line in result]
            