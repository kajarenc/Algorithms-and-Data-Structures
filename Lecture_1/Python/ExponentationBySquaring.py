import sys
import time
import random

def NaiveExponentationBySquaring(a, n, mod):
	res = long(1)
	for i in xrange(n):
		res = res * a % mod

	return res

def RecursiveExponentationBySquaring(a, n, mod):
	if n == 0:
		return 1
	if n == 1:
		return a % mod
	if n % 2 == 1:
		return a * RecursiveExponentationBySquaring(a, n - 1, mod) % mod
	else:
		temp = RecursiveExponentationBySquaring(a, n / 2, mod)

		return temp * temp % mod

def IterativeExponentationBySquaring(a, n, mod):
	result = long(1)
	while n > 0:
		if n & 1:
			result = result * a % mod
		a = a * a % mod
		n >>= 1

	return result

def main():
	test_count = 100
	for test_id in xrange(test_count):
		a = random.randint(1, 1000)
		n = random.randint(1, 1000000)
		mod = random.randint(1, 1000)

		naive_res = NaiveExponentationBySquaring(a, n, mod)

		recursive_begin = time.clock()
		recursive_res = RecursiveExponentationBySquaring(a, n, mod)
		recursive_end = time.clock()

		iterative_begin = time.clock()
		iterative_res = IterativeExponentationBySquaring(a, n, mod)
		iterative_end = time.clock()

		if naive_res != iterative_res or naive_res != recursive_res:
			sys.stdout.write(('FAILURE: NaiveRes({naive}) IterativeRes({iterative}) ' +
				'RecursiveRes({recursive}).\n').format(naive=naive_res,
				                                       iterative=iterative_res,
				                                       recursive=recursive_res))
		else:
			iterat = round((iterative_end - iterative_begin) / 1000.0, 2)
			recursive = round((recursive_end - recursive_begin) / 1000.0, 2)
			sys.stdout.write(('SUCCESS.\nIterativeRunningTime({iterat}) vs ' +
				'RecursiveRunningTime({recursive}).\n').format(
				iterat=iterat,
				recursive=recursive))

if __name__ == '__main__':
	main()
