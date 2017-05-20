def stairs(n):
	if n<1:
		return 0
	if n==1:
		return 1
	if n==2:
		return 2
	if n==3:
		return 4
	return stairs(n-1)+stairs(n-2)+stairs(n-3)
# @staticmethod
def opt_stairs(n,m):
	if n<=1:
		return n
	res = 0
	i=1
	while i<=n and i<=m:
		res+=opt_stairs(n-i,m)
		i+=1
	return res

if __name__=='__main__':
	# print("{} ways".format(stairs(int(raw_input()))))
	print("{} ways".format(opt_stairs(int(raw_input())+1,3)))