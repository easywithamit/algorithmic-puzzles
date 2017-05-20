def count_digit(num,d):
	c = 0
	while num!=0:
		if num%10==d:
			c+=1
		num/=10
	return c
def count_digits_improved(n,d):
	n1=n
	c=0
	f=1
	r_collect = 0
	while n1!=0:
		r = n1%10
		n1 = n1/10
		c+=n1*f
		if r>d:
			c+=f
		elif r==d:
			c += r_collect+1
		r_collect = r*f+r_collect
		f*=10
	return c

def count_digits(n,d):
	c = 0
	for i in xrange(1,n+1):
		c += count_digit(i,d)
	return c
if __name__=='__main__':
	n = int(raw_input())
	d = int(raw_input())
	print("Standard:")
	print(count_digits(n,d))
	print("Our approach")
	print(count_digits_improved(n,d))
