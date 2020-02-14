class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        dict_order = {c:i for i,c in enumerate(order)}
        
        if len(words) < 1:
            return True
        
        for w in range(len(words)):
            if w+1 > len(words):
                return False
                
            left = {i:c for i,c in enumerate(words[w])}
            right = {i:c for i,c in enumerate(words[w + 1])}
            
            n = len(left)
            
            if len(left) > len(right):
                n = len(right)
            for i in range(n):
                if dict_order[left[i]] <= dict_order[right[i]]:
                    continue
                else:
                    return False

if __name__ == "__main__":
    print(Solution.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
    