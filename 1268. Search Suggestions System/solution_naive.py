class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        result = []
        query = ""
        
        for ch in searchWord:
            query += ch
            
            result.append([x for x in products if x.startswith(query)][:3])
            
        return result
