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
                    free_space -= 1
                # add spaces
                word_it = cycle(current_line)
                word_in_line = next(word_it)
                word_idx = 0
                while free_space > 0:
                    if ' ' in word_in_line:
                        current_line[word_idx] += ' '
                        free_space -= 1
                    word_in_line = next(word_it)
                    word_idx = (word_idx + 1) % len(current_line)
                    
                result.append("".join(current_line))
                current_line = [word]
        
        # align last line
        current_line = "".join(current_line)
        while len(current_line) != maxWidth:
            current_line += ' '
        result.append(current_line)
                
        return result
            