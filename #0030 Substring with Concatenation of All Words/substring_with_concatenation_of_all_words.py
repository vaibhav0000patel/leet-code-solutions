from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]):
        locations = []
        
        if not words:
            return locations
        
        word_length = len(words[0])
        match_length = word_length*len(words)
        index = 0

        while index < len(s)-match_length+1:

            if s[index:index+word_length] not in words:
                index+=1
                continue

            words_clone = list(words)
            saved_index = index
            while s[index:index+word_length] in words_clone:
                words_clone.remove(s[index:index+word_length])
                index += word_length
            if not words_clone:
                locations.append(saved_index)
            index = saved_index+1
                
        return locations


print ("Solution\""+str(Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",["fooo","barr","wing","ding","wing"]))+"\"")