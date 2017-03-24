def getMinCoins(coins,s):
	temp = s
	min_coins = 0
	for coin in coins:
		if temp==0:
			break
		if coin<=temp:
			min_coins += (temp/coin)
			temp = temp%coin
			print("{} coins , left: {}".format(coin,temp))
	if temp==0:
		return min_coins
	else:
		return -1
def getMinCoinsDP(coins,value):
	result = 300000
	if value==0:
		return 0
	else:
		for coin in coins:
			if value >= coin:
				sub_result = getMinCoinsDP(coins,value-coin)
				if sub_result==0 and sub_result+1<result:
					result+=1
	return result

# def getMinCoinsDP(s,value={}:
	
# 	if s in value:
# 		return value[s]
# 	if s == 5:
# 		value[s]= 1
# 	elif s == 3:
# 		value[s] = 1
# 	elif s == 1:
# 		value[s] = 1
# 	else:
# 		value[s]=min(1+getMinCoinsDP(s-1,value),getMinCoinsDP(s,value))


if __name__=='__main__':
	d = [int(x) for x in raw_input().split()]
	s = int(raw_input())
	print("min coins out of {} to get {} : {} ".format(d,s,getMinCoinsDP(d,s)))
