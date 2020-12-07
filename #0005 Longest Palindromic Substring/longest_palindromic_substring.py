class Solution:
	
	def checkPalindrome(self,s):
		return s==s[::-1]

	def longestPalindrome(self, s):
		lens = len(s)
		if(lens==1):
			return s
		longestSubstring = ""
		longestSubstringlen = 0
		for i in range(lens):
			for j in range(i+1,lens+1):
				ss = s[i:j]
				lenss = len(ss)
				if self.checkPalindrome(ss) and lenss>longestSubstringlen:
					longestSubstring = ss
					longestSubstringlen = lenss
		return longestSubstring