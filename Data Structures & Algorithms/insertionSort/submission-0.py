# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        answer = []
        for i in range(len(pairs)):
            j = i-1
            while(j >= 0 and pairs[j].key > pairs[i].key):
                temp = pairs[i]
                pairs[i] = pairs[j]
                pairs[j] = temp
                j -= 1
                i -= 1
            answer.append(pairs.copy())
            

            
            
        return answer
        