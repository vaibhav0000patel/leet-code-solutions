class Solution:
	def convert(self, s, numRows):
		if numRows==1:
			return s
		ds = []
		for i in range(numRows):
			ds.append([])
		
		down = 0
		go=True
		
		i=0
		lens = len(s)
		while(i<lens):
			while go:
				if down<numRows and i<lens:
					ds[down].append(s[i])
					i+=1
					down+=1
				else:
					down-=1
					go=False
			while not go:
				if down>0 and i<lens:
					down-=1
					ds[down].append(s[i])
					i=i+1
				else:
					down+=1
					go=True
		return "".join(["".join(row) for row in ds])