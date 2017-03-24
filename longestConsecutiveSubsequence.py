def longest_consecutive_subsequence(a):
	all_elements = set()
	length_max_sub_seq = 0
	for e in a:
		all_elements.add(e)
	l = len(a)
	for i in xrange(l):
		val = a[i]
		if val-1 not in all_elements:
			temp = val
			while temp in all_elements:
				temp+=1
			length_max_sub_seq = max(length_max_sub_seq,temp-val)
	return length_max_sub_seq


if __name__=='__main__':
	arr = [int(x) for x in raw_input().split()]
	print(longest_consecutive_subsequence(arr))