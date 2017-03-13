def getSteps(a,b):
	steps = 0
	while a!=1 and b!=1:
		if a>b:
			steps += a/b
			a = a%b
		else:
			steps += b/a
			b = b%a
	if a==1:
		steps += (b-1)
		return steps
		b=1
	elif b==1:
		steps += (a-1)
		return steps
		a=1
	return -1
if __name__=='__main__':
	a = int(raw_input())
	b = int(raw_input())
	steps = getSteps(a,b)
	if steps==-1:
		print("Not in series")
	else:
		print("{} steps for reaching the numbers({},{})".format(steps,a,b))