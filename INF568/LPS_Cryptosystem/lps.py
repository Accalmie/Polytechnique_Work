import util as u
import os.path





def get_public_key(pub_key):
	if not os.path.isfile(pub_key):
		print("There are no public key available")
		return None

	with open(pub_key, 'r') as f:
		lines = f.readlines()
		
		n = int(lines[1])
		k = int(lines[2])
		q = int(lines[3])

		lines = lines[4::]

		rows = []

		for i in range(len(lines)):
			row = get_vector(lines[i])
			rows.append(row)

		A = u.transpose(rows)

		f.close()

	return A, n, k, q


def get_vector(line):
	vector = []
	s = line.split(' ')
	for n in s:
		vector.append(int(n))
	return vector


def get_private_key(priv_key):
	if not os.path.isfile(priv_key):
		print("There are no private key available")
		return None

	with open(priv_key, 'r') as f:
		lines = f.readlines()
		
		n = int(lines[1])
		k = int(lines[2])

		lines = lines[3::]

		S = []

		for i in range(len(lines)):
			si = get_vector(lines[i])
			S.append(si)


		f.close()

	return S, n, k


def encrypt(m, A, q, n, k):
	r = u.random_bit_vector(n)
	tA = u.transpose(A)

	coeff = (q-1) / 2

	alpha = (u.matrix_vector(tA, r, q))

	beta = [0 for i in range(n)]

	for i in range(k):
		mi = coeff*m[i]
		beta.append(mi)

	c = []

	for i in range(len(alpha)):
		ti = alpha[i] + beta[i]
		ti %= q
		if ti > ((q - 1) / 2):
			ti -= q
			#print("Correction")
		if ti < -((q-1)/2):
			ti += q
			#print("Correction")
		c.append(ti)

	#print("Encryption completed")
	return c


def decrypt(c, S, q, n, k):
	v = []
	w = []

	m = []

	for i in range(n):
		v.append(c[i])

	for i in range(k):
		w.append(c[n + i])

	for i in range(k):
		yi = (u.scalar_product(v, S[i]) - w[i]) % q

		if abs(yi) < q/4:
			mi = 0
		else:
			mi = 1

		m.append(mi)

	#print("Decrypted")

	return m


def test_vector():
	a = '45 25 36 56 45'
	v = get_vector(a)
	print(v)

def test():
	test = 'coucou'

	m = u.string_to_binary(test)

	A, n, k, q = get_public_key()

	c = encrypt(m, A, q, n, k)

	print("Encrypted to : " + str(c))

	S, n, k = get_private_key()

	dec = decrypt(c, S, q, n, k)
	print(len(dec))
	final_dec = u.binary_to_string(dec)

	print("Decrypted to : " + final_dec)

def test2():
	A, n, k, q = get_public_key('test-8-40-401.pub')
	S, N, K = get_private_key('test-8-40-401.priv')

	n = len(A)
	m = len(A[0])
	
	modulus = q ** m

	total_sum = 0

	print(S[0])
	print(A)

	for i in range(N):
		if S[0][i] == 1:
			total_sum += u.sum_vector_base_q(A[i], q)

	total_sum %= modulus
	t = A[N]

	test_sum = 0
	for i in range(m):
		test_sum += t[i]*(q**i)

	print(test_sum)
	print(total_sum)

	#print("Before modulus : " + str(total_sum))


if __name__ == '__main__':
	# test_vector()
	# test()
	test2()



