class Solution:
	def lengthOfLongestSubstring(self, s):
		lens = len(s)
		if(lens==1):
			return lens
			
		longestSubstringlen,currentSubstringlen,substringStarts = 0,0,0
		currentSubstring = ""
		
		i = 0
		while(i<lens):
			if s[i] not in currentSubstring:
				currentSubstring += s[i]
				currentSubstringlen += 1
				if currentSubstringlen>longestSubstringlen:
					longestSubstringlen = currentSubstringlen
				i=i+1
			else:
				substringStarts = substringStarts+currentSubstring.find(s[i])+1
				i = substringStarts
				currentSubstringlen = 0
				currentSubstring = ""
				
		return longestSubstringlen