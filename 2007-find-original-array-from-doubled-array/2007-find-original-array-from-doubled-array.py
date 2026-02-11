from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        original = []
        changed = sorted(changed)
        changed_counts = Counter(changed)

        for i in changed: 
            
            if len(original) == len(changed) // 2:
                break
            if i * 2 in changed_counts and changed_counts[i] != 0 and changed_counts[i * 2] != 0:
                
                if i * 2 == i and changed_counts[i] < 2:
                    continue
                
                changed_counts[i] -= 1
                changed_counts[i * 2] -= 1
                original.append(i)
                
        if len(original) == len(changed) / 2:
            return original
        return []
        

        