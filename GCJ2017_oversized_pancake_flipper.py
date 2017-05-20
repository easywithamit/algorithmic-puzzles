def is_happy_flippable(s,k):
	pass
if __name__=='__main__':
	T = int(raw_input())
	T1=T
	while T:
		n = [v for v in raw_input()]
		S = n[:-1]
		K = int(n[-1])
		result = is_happy_flippable(S,K)
		T-=1
		if result:
			print("Case #{}: {}".format((T1-T+1),result))
		else:
			print("Case #{}: {}".format((T1-T+1),"Impossible"))
