
def digSum(n) :

	if n == 0 :
		return 0

	elif n % 9 == 0 :
		return 9

	else :
		return n % 9

def powerDigitSum(a, n) :

	res = 1
	while(n) :

		if n %2 == 1 :
			res = res * digSum(a)
			res = digSum(res)

		a = digSum(digSum(a) * digSum(a))
		n //= 2

	return res


if __name__ == "__main__" :

	a, n = 9, 4
	print(powerDigitSum(a, n))

