def findMaxPos(a):
	length = len(a)
	max = a[0]
	max_pos = 0
	for i in xrange(1,length):
		if max<a[i]:
			max_pos = i
			max = a[i]
	return max_pos

def getMinMoves(d,count_moves = 0):
	maximum = findMaxPos(d)
	if d[maximum]==0:
		return count_moves
	L = [0]*length
	R = [0]*length
	for i in xrange(1,length):
		L[i] = L[i-1]+d[i-1]
	for i in xrange(length-2,-1,-1):
		R[i] = R[i+1]+d[i+1]
	print("L = {}".format(L))
	print("R = {}".format(R))
	print("Max position = {}".format(maximum))
	if maximum>0:
		d[maximum] = d[maximum]+ L[maximum]
		d[maximum-1] = d[maximum-1] - L[maximum]
		count_moves = count_moves - L[maximum]
	if maximum<length-1:
		d[maximum] = d[maximum]+ R[maximum]
		d[maximum+1] = d[maximum+1] - R[maximum]
		count_moves = count_moves - R[maximum]
	print("count moves : {}".format(count_moves))
	print("d = {}".format(d))
	return getMinMoves(d,count_moves)

if __name__=='__main__':
	initial = [int(x) for x in raw_input().split()]
	final = [int(x) for x in raw_input().split()]
	length = len(initial)
	if sum(initial)==sum(final):
		diff = [initial[i]-final[i] for i in xrange(0,length)]
		print diff
		print("Minimum moves: {}".format(getMinMoves(diff)))
