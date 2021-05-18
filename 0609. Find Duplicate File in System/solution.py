class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicates = collections.defaultdict(list)
        result = []
        
        for path in paths:
            tokens = path.split(' ')
            base_path, files = tokens[0], tokens[1:]
            
            for file in files:
                filename, contents = file[:-1].split('(')
                duplicates[contents].append(base_path + '/' + filename)
                
        for content in duplicates:
            if len(duplicates[content]) > 1:
                result.append(duplicates[content])
        
        return result
                
