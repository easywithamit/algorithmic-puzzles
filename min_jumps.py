max=99999
def min_jumps(a,i):
	if a[i]==0:
		return max
	if i==len(a)-1:
		return 0
	li=[]
	for j in xrange(1,a[i]-1):
		li.append(min_jumps(a,i+a[i]))
	return 1+min(li)

if __name__=='__main__':
	arr = [1,3,5,8,9,2,6,7,6,8,9]
	print(min_jumps(arr,0))