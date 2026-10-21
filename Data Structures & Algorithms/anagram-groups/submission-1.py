class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_of_anagrams = []
        map_of_anagrams = {}

        character_count = [0] * 26
        for s in strs:
            for char in s:
                character_count[ord(char) - ord('a')] += 1
            if tuple(character_count) not in map_of_anagrams:
                map_of_anagrams[tuple(character_count)] = [s]
            else:
                map_of_anagrams[tuple(character_count)].append(s)
            character_count = [0] * 26

        
        for key in map_of_anagrams:
            list_of_anagrams.append(map_of_anagrams[key])
            







        return list_of_anagrams
        