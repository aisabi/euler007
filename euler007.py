#first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#so that the 6th prime is 13What is the nth prime number?
#nthPrime(6) should return 13.

import sympy #Python library for symbolic mathematics.


def nthPrime(n):
	nombrePremiers = list(sympy.primerange(0, 105000))
	for number in nombrePremiers:
		position = nombrePremiers[n - 1] # python counts position from 0 
	print('The Prime Number in position',n,'is :',position)

nthPrime(1000)
