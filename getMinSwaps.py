def getMinSwaps(pattern):
	l = len(pattern)
	p1 = 'WB'* (l/2)
	p2 = 'BW' * (l/2)
	c1=c2=0
	for i in xrange(l):
		if pattern[i]!=p1[i]:
			c1+=1
		if pattern[i]!=p2[i]:
			c2+=1
	c = min(c1,c2)
	return c/2

if __name__=='__main__':
	pattern = raw_input()
	print(getMinSwaps(pattern))