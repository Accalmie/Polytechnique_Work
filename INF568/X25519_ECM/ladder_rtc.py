import util as u



def ladder(N, a24, m, P):
	X = P[0]
	X = X % N
	#X = long(X, 16)
	
	x0P = 1
	x0Q = 0
	x1P = X
	x1Q = 1
	swap = 0

	#m = long(m, 16)

	i = m.bit_length() - 1

	while i != -1:
		swap_bit = (m >> i) & 1
		swap = swap_bit ^ swap

		i = i -1
		# Swap pour le xDBL
		x0P, x1P = u.SWAP(swap, (x0P, x1P))
		x0Q, x1Q = u.SWAP(swap, (x0Q, x1Q))

		swap = swap_bit

		A = (x0P + x0Q) % N
		AA = pow(A, 2, N)
		B = (x0P - x0Q) % N
		BB = pow(B, 2, N)

		E = (AA - BB) % N

		C = (x1P + x1Q) % N
		D = (x1P - x1Q) % N

		DA = (D * A) % N
		CB = (C * B) % N

		x1P = pow((DA + CB) % N, 2, N)
		x1Q = (X * pow(((DA - CB) % N), 2, N)) % N

		x0P = (AA * BB) % N
		inter = a24 * E % N
		x0Q = (E * ((BB + ((a24 * E) % N)) % N)) % N

		#raw_input()

	x0P, x1P = u.SWAP(swap, (x0P, x1P))
	x0Q, x1Q = u.SWAP(swap, (x0Q, x1Q))
 	
	#print ("Ladder returns " + str(x0P) + "," + str(x0Q))

	return x0P, x0Q

def test():
	# First curve:
	p = 101
	a24 = 38

	x1 = (2,2,1)

	print("TEST 1")
	alpha = (ladder(p, a24, 2, x1))
	beta = (ladder(p, a24, 3, x1))
	gamma = (ladder(p, a24, 77, x1))

	print(alpha[0] * (pow(alpha[1], p-2, p)) % p)
	print(beta[0] * (pow(beta[1], p-2, p)) % p)
	print(gamma[0] * (pow(gamma[1], p-2, p)) % p)

# ## check these (on (X,Z)-coordinates only):
# [2]P = (70:81:1)
# [3]P = (59:61:1)
# [77]P = (8:90:1)


# Second curve:
	p = 1009
	a24 = 171

	x1 = (7, 207, 1)

	print("TEST 2")
	print(ladder(p, a24, 2, x1))
	print(ladder(p, a24, 3, x1))
	print(ladder(p, a24, 5, x1))
	print(ladder(p, a24, 34, x1))
	print(ladder(p, a24, 104, x1))
	print(ladder(p, a24, 947, x1))

## check these (on (X,Z)-coordinates only):
# [2]P = (284:3:1)
# [3]P = (759:824:1)
# [5]P = (1000:308:1)
# [34]P = (286:675:1)
# [104]P = (810:312:1)
# [947]P = (755:481:1)



def xDBL(xP, zP, A, N):
	c = 121665

	t1 = xP + zP % N
	alpha = pow(t1, 2, N)
	t2 = xP - zP % N
	beta = pow(t2, 2, N)
	gamma = alpha -beta % N
	x2P = alpha * beta % N
	z2P = (gamma * (beta + c*gamma % N)) % N
	
	return x2P, z2P


def xADD(xMinus, xP, zP, xQ, zQ, N):
	t1 = xP + zP % N
	t2 = xP - zP % N
	t3 = xQ + zQ % N
	t4 = xQ - zQ % N	
	alpha = t4 * t1 % N
	beta = t3 * t2 % N

	xPlus = pow(alpha + beta % N, 2, N)
	yPlus = (xMinus * pow(alpha - beta % N, 2, N)) % N

	return xPlus, yPlus

if __name__ == '__main__':
	test()